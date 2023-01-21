from csv import DictReader
from json import loads

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
