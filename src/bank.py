from json import dumps
from src.helpers import read_extract


class Bank:
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def extract(self):
        data = read_extract(self.name)
        concepts = {}
        with open(f'conceptos/{self.name}.json', 'w') as conceptos:
            for line in data:
                concepts[line[self.key]] = '@'
        
            conceptos.write(dumps(concepts, sort_keys=True, indent=4))
        print(f"Done extracting curated concepts for {self.name}")

    def translate():
        """
        nombre banco
            fecha | codigo | concepto | debito | credito | saldo
        """
        pass