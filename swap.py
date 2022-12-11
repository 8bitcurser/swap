from csv import DictReader, DictWriter


def read_supervielle_flow():
    with open('extractos/supervielle_flow.csv', newline='\r\n') as sup:
        file = sup.readlines()
        data = DictReader(file, delimiter=';')
        data = [*data]
        return data

if __name__ == '__main__':
    extract = read_supervielle_flow()
    conceptos_set = {line['Concepto'] for line in extract}
    with open('conceptos/supervielle.csv', 'w', newline='\n') as conceptos:
        fieldnames=['conceptos']
        csv = DictWriter(conceptos, fieldnames=fieldnames)
        csv.writeheader()
        for concepto in conceptos_set:
            csv.writerow({'conceptos': concepto})
    
    print("Done extracting curated concepts")