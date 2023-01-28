from csv import DictReader

from pandas import read_csv


def read_extract(extract_name):
    with open(f'extractos/{extract_name}.csv', newline='\r\n') as sup:
        file = sup.readlines()
        data = DictReader(file, delimiter=';')
        data = [*data]
        return data

def read_concept(bank_name):
    with open(f'conceptos/{bank_name}.csv', newline='\n') as sup:
        file = sup.readlines()
        data = DictReader(file, delimiter=',')
        data = [*data]
        cleaned = {}
        for record in data:
            cleaned[record['CONCEPTOS']] = {
                'ID': record['ID'],
                'ASTOR': record['CONCEPTO ASTOR']
            }
        return cleaned

def convert_csv_to_xls(file_path, destination='recategorization'):
    file = read_csv(file_path)
    file_name = file_path.split('/')[-1].split('.')[0]
    file.to_excel(f'{destination}/{file_name}.xlsx', index=None, header=True)

