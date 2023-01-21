from csv import DictWriter

from src.bank import Bank
from src.constants import concepts
from src.helpers import read_concept, read_extract


class Supervielle(Bank):
    def recategorization(self):
        extract_data = read_extract(self.name)
        concepts_bank = read_concept(self.name)
        with open(f'recategorization/{self.name}.csv', 'w', newline='\n') as transform:
            fieldnames=['fecha', f'concepto_{self.name}', 'concepto_astor', 'codigo', 'debito', 'credito', 'saldo']
            csv = DictWriter(transform, dialect='excel', fieldnames=fieldnames)
            csv.writeheader()
            for line in extract_data:
                inner_concept = line['Concepto']
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        f'concepto_{self.name}': inner_concept,
                        'concepto_astor': concepts_bank[inner_concept]['ASTOR'],
                        'codigo': concepts_bank[inner_concept]['ID'],
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo']

                    }
                )


supervielle = Supervielle('supervielle', 'Concepto')