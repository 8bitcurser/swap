from csv import DictWriter

from src.bank import Bank
from src.constants import concepts
from src.helpers import read_concept, read_extract, convert_csv_to_xls


class Supervielle(Bank):
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
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        f'concepto_{self.name}': inner_concept,
                        'concepto_astor': concepts_bank[inner_concept]['ASTOR'],
                        'codigo': id,
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo'],
                        'objetivo': f"{line['Concepto']} - {line['Detalle']}" if id in ['1', '2', '6', '8', '12'] else ""
                    }
                )
        convert_csv_to_xls(file_path)


supervielle = Supervielle('supervielle', 'Concepto')