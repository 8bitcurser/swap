from csv import DictWriter

from helpers import read_concept, read_extract
from constants import concepts

"""
nombre banco
    fecha | codigo | concepto | debito | credito | saldo
"""
def translate():
    banks = ['supervielle']
    for bank in banks:
        extract_data = read_extract(bank)
        concepts_bank = read_concept(bank)
        with open(f'translations/{bank}.csv', 'w', newline='\n') as transaltion:
            fieldnames=['fecha', 'codigo', 'concepto', 'debito', 'credito', 'saldo']
            csv = DictWriter(transaltion, dialect='excel', fieldnames=fieldnames)
            csv.writeheader()
            for line in extract_data:
                codigo = concepts_bank.get(line['Concepto'])
                if codigo is None:
                    continue
                concepto = concepts[codigo]
                csv.writerow(
                    {
                        'fecha': line['Fecha'],
                        'codigo': codigo,
                        'concepto': concepto,
                        'debito': line['Débito'],
                        'credito': line['Crédito'],
                        'saldo': line['Saldo']

                    }
                )