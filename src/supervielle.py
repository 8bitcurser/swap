from csv import DictWriter
from re import match

from src.bank import Bank
from src.helpers import read_concept, read_extract, convert_csv_to_xls


class Supervielle(Bank):
    def _objective_parser(self, line, id):
        if id == "12":
            cuit = match(r"/(?<![\s:-])*\b(\d{11})\b(?!\s)*", line['Detalle'])
            objective = cuit.group() if cuit is not None else ""
        else:
            check_num = line['Detalle'].replace("Número De Cheque: ", '')
            print(line['Concepto'])
            if 'Falla Técnica' in line['Concepto']:
                objective = f"{check_num} // Falla Técnica"
            else:
                objective = check_num
        return objective

    def recategorization(self):
        extract_data = read_extract(self.name)
        concepts_bank = read_concept(self.name)
        file_path = f'recategorization/{self.name}.csv'
        with open(file_path, 'w', newline='\n') as transform:
            fieldnames=['fecha', f'concepto_{self.name}', 'concepto_astor', 'codigo', 'debito', 'credito', 'saldo', 'objetivo']
            csv = DictWriter(transform, dialect='excel', fieldnames=fieldnames)
            csv.writeheader()
            for line in extract_data:
                inner_concept = line['Concepto']
                id = concepts_bank[inner_concept]['ID']
                objective = self._objective_parser(line, id) if id in ["1", "12"] else ""
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        f'concepto_{self.name}': inner_concept,
                        'concepto_astor': concepts_bank[inner_concept]['ASTOR'],
                        'codigo': id,
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo'],
                        'objetivo': objective
                    }
                )
        convert_csv_to_xls(file_path)


supervielle = Supervielle('supervielle', 'Concepto')