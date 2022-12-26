from csv import DictWriter

from src.helpers import read_concept, read_extract
from src.constants import concepts

"""
nombre banco
    fecha | codigo | concepto | debito | credito | saldo
"""
def translate():
    banks = ['bbva']
    for bank in banks:
        extract_data = read_extract(bank)
        concepts_bank = read_concept(bank)
        with open(f'translations/{bank}.csv', 'w', newline='\n') as transaltion:
            fieldnames=['fecha', 'codigo', 'concepto', 'debito', 'credito', 'saldo']
            csv = DictWriter(transaltion, fieldnames=fieldnames)
            csv.writeheader()
            watch_flag = False
            for line in extract_data:
                code_map = concepts_bank[line['Codigo']]
                code = code_map['code']
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