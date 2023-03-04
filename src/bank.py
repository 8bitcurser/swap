from dataclasses import dataclass, field
from src.constants import concepts
from src.helpers import read_concept, read_extract, read_recat, convert_csv_to_xls


@dataclass
class Bank:
    name: str
    key: str
    cuil: int = 0
    extract_file: str = ""
    extract_data: list = field(default_factory=list)
    enriched_extract_data: list = field(default_factory=list)
    concepts_map: dict = field(default_factory=dict)
    total_by_category: dict = field(default_factory=dict)

    def _amount_parser(self, amount):
        return float(amount.replace('.', '').replace(',', '.'))

    def _objective_parser(self, line, id):
        pass

    def _enrich(self):
        """
            This step has a previous requirement which is to make the input csv into a format readable by
            enrich.
            fecha | codigo | concepto | debito | credito | saldo | objetivo
        """
        for line in self.extract_data:
            bank_concept = line['Concepto']
            id = self.concepts_map[bank_concept]
            objective = self._objective_parser(line, id) if id in [1, 12] else ""
            self.enriched_extract_data.append(
                {
                    'fecha': line['Fecha'],
                    f'concepto_{self.name}': bank_concept,
                    'concepto_astor': concepts[id],
                    'codigo': id,
                    'debito': line['Débito'],
                    'credito': line['Crédito'],
                    'saldo': line['Saldo'],
                    'objetivo': objective
                }
            )
    
    def _sum_by_bank_category(self):
        for record in self.enriched_extract_data:
            concepto = record['concepto_astor']
            monto = record['credito'] if not record['debito'] else record['debito']
            monto = self._amount_parser(monto)
            if self.total_by_category.get(concepto) is not None:
                self.total_by_category[concepto] += monto
            else:
                self.total_by_category[concepto] = monto
    
    def load(self):
        self.extract_data = read_extract(f'{self.name}')
        self._enrich()
        self._sum_by_bank_category()
    
    def get_thirdparty_transfers(self):
        data = self.enriched_extract_data
        transfers = [
            line for line in data if line['codigo'] == 12 and line['objetivo'] != self.cuil and line['debito']]
        transfers_by_cuil = {
        }
        for transfer in transfers:
            thirdparty_cuil = transfer['objetivo']
            monto = self._amount_parser(transfer['debito'])
            if transfers_by_cuil.get(thirdparty_cuil) is not None:
                transfers_by_cuil[thirdparty_cuil] += monto
            else:
                transfers_by_cuil[thirdparty_cuil] = monto

        file_name = f'transfers/{self.name}.csv'
        with open(file_name, 'w') as post:
            post.write("cuil,monto\n")
            for transfer in transfers_by_cuil:
                post.write(f"{transfer},{'{:.2f}'.format(transfers_by_cuil[transfer])}\n")
        
        convert_csv_to_xls(file_name, destination='transfers')