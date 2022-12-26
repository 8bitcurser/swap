import re
from json import dumps

from helpers import read_extract


def extract():
    concepts = {}
    with open(f'conceptos/supervielle.json', 'w') as conceptos:
        data = read_extract('supervielle')
        conceptos_set = {line['Concepto'].strip() for line in data}
        for concepto in conceptos_set:
            concepts[concepto] = '@'
        conceptos.write(dumps(concepts, sort_keys=True, indent=4))
    
    print(f"Done extracting curated concepts for supervielle")
