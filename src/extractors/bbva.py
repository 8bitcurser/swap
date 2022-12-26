import re
from collections import defaultdict
from json import dumps
from src.helpers import read_extract


def extract():
    data = read_extract('bbva')
    concepts = defaultdict(dict)
    with open(f'conceptos/bbva.json', 'w') as conceptos:
        for line in data:
            curated_concept = re.sub(r'(\d+/\d+/\d+)|(\d{3,})', '', line['Concepto']).strip()
            concepts[line['Codigo']]['concepts'] = curated_concept
            concepts[line['Codigo']]['code'] = '@'
        
        conceptos.write(dumps(concepts, sort_keys=True, indent=4))
    
    print(f"Done extracting curated concepts for bbva")
