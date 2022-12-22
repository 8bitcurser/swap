from csv import DictReader
from json import loads

def read_extract(extract_name):
    with open(f'swap/extractos/{extract_name}.csv', newline='\r\n') as sup:
        file = sup.readlines()
        data = DictReader(file, delimiter=';')
        data = [*data]
        return data

def read_concept(bank_name):
    with open(f'swap/conceptos/{bank_name}.json') as sup:
        file = sup.read()
        return loads(file)
