import re
from json import dumps

from helpers import read_extract


if __name__ == '__main__':
    extracts = {
        # 'supervielle': {'data': read_extract('supervielle_flow')},
        'bbva': {'data': read_extract('bbva')}
    }
    
    for bank in extracts:
        concepts = {}
        with open(f'conceptos/{bank}.json', 'w') as conceptos:
            conceptos_set = {re.sub(r'(\d+/\d+/\d+)|(\d{3,})', '', line['Concepto']).strip() for line in extracts[bank]['data']}
            for concepto in conceptos_set:
                concepts[concepto] = '@'
            conceptos.write(dumps(concepts))
    
    print(f"Done extracting curated concepts for {extracts.keys()}")
