from csv import DictWriter

from src.bank import Bank
from src.constants import concepts
from src.helpers import read_concept, read_extract


class BIND(Bank):
    def translate(self):
        extract_data = read_extract(self.name)
        concepts_bank = read_concept(self.name)
        with open(f'translations/{self.name}.csv', 'w', newline='\n') as translation:
            fieldnames=['fecha', 'codigo', 'concepto', 'debito', 'credito', 'saldo']
            csv = DictWriter(translation, dialect='excel', fieldnames=fieldnames)
            csv.writeheader()
            for line in extract_data:
                codigo = concepts_bank.get(line[self.key])
                if codigo is None or codigo == '@':
                    continue
                concepto = concepts[codigo]
                csv.writerow(
                    {
                        'fecha': line['Fecha Operación'],
                        'codigo': codigo,
                        'concepto': concepto,
                        'debito': line['Importe'],
                        'credito': '-',
                        'saldo': line['Saldo']

                    }
                )


bind = BIND('bind', 'Descripción')