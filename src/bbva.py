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
                code = concepts_bank[line[self.key]]
                # ignore undefined ones
                if isinstance(code, str):
                    continue
                # bbva triad activates
                if code == '898':
                    watch_flag = True
                # deactivate flag when triad or duo is over
                if watch_flag and isinstance(code, int):
                    watch_flag = False
                # if triad activated use correct code if not default to normal
                if isinstance(code, list) and watch_flag:
                    code = code[1]
                elif isinstance(code, list) and not watch_flag:
                    code = code[0]
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        'codigo': code,
                        'concepto': concepts[str(code)],
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo']

                    }
                )

bbva = BBVA('bbva', 'Codigo')