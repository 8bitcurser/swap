import re
from collections import defaultdict
from json import dumps
from src.helpers import read_extract


def extract(bank, key):
    data = read_extract(bank)
    concepts = {}
    with open(f'conceptos/{bank}.json', 'w') as conceptos:
        for line in data:
            concepts[line[key]] = '@'
        
        conceptos.write(dumps(concepts, sort_keys=True, indent=4))
    
    print(f"Done extracting curated concepts for {bank}")
