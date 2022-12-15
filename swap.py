import re
from csv import DictReader, DictWriter


def read_extract(extract_name):
    with open(f'swap/extractos/{extract_name}.csv', newline='\r\n') as sup:
        file = sup.readlines()
        data = DictReader(file, delimiter=';')
        data = [*data]
        return data

if __name__ == '__main__':
    extracts = {
        'supervielle': {'data': read_extract('supervielle_flow')},
        'bbva': {'data': read_extract('bbva')}
    }
    
    for bank in extracts:
        with open(f'swap/conceptos/{bank}.csv', 'w', newline='\n') as conceptos:
            fieldnames=['conceptos']
            csv = DictWriter(conceptos, fieldnames=fieldnames)
            csv.writeheader()
            conceptos_set = {re.sub(r'(\d+/\d+/\d+)|(\d{3,})', '', line['Concepto']).strip() for line in extracts[bank]['data']}
            for concepto in conceptos_set:
                csv.writerow({'conceptos': concepto})
    
    print(f"Done extracting curated concepts for {extracts.keys}")