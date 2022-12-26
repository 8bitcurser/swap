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
            previous_concepts = concepts[line['Codigo']].get('concepts')
            if previous_concepts is not None:
                concepts[line['Codigo']]['concepts'].add(curated_concept)
            else:
                concepts[line['Codigo']]['concepts'] = set()
            concepts[line['Codigo']]['code'] = '@'
        
        for concept in concepts:
            concepts[concept]['concepts'] = list(concepts[concept]['concepts'])
        conceptos.write(dumps(concepts, sort_keys=True, indent=4))
    
    print(f"Done extracting curated concepts for bbva")
