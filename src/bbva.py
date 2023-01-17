from csv import DictWriter

from src.bank import Bank
from src.constants import concepts
from src.helpers import read_concept, read_extract


class BBVA(Bank):
    def translate(self):
        extract_data = read_extract(self.name)
        concepts_bank = read_concept(self.name)
        with open(f'translations/{self.name}.csv', 'w', newline='\n') as translation:
            fieldnames=['fecha', 'codigo', 'concepto', 'debito', 'credito', 'saldo']
            csv = DictWriter(translation, dialect='excel', fieldnames=fieldnames)
            csv.writeheader()
            watch_flag = False
            for line in extract_data:
                internal_code = line[self.key]
                external_code = concepts_bank[internal_code]['code']
                # ignore undefined ones
                if isinstance(external_code, str):
                    continue
                # deactivate flag when triad or duo is over
                if watch_flag and isinstance(external_code, int):
                    watch_flag = False
                # bbva triad activates
                if internal_code == '898':
                    watch_flag = True

                # if triad activated use correct code if not default to normal
                if isinstance(external_code, list) and watch_flag:
                    external_code = external_code[1]
                elif isinstance(external_code, list) and not watch_flag:
                    external_code = external_code[0]
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        'codigo': external_code,
                        'concepto': concepts[str(external_code)],
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo']

                    }
                )

bbva = BBVA('bbva', 'Codigo')