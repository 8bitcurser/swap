from src.helpers import read_recat

class Bank:
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def recategorization(self):
        """
        nombre banco
            fecha | codigo | concepto | debito | credito | saldo
        """
        pass
    
    def post_processing(self):
        cat_sum = {}
        data = read_recat(f'{self.name}.csv')
        for record in data:
            concepto = record['concepto_astor']
            monto = record['credito'] if not record['debito'] else record['debito']
            monto = float(monto.replace('.', '').replace(',', '.'))
            if cat_sum.get(concepto) is not None:
                cat_sum[concepto] += monto
            else:
                cat_sum[concepto] = monto
        with open(f'post_process/{self.name}.csv', 'w') as post:
            post.write("'concepto','monto'\n")
            for cat in cat_sum:
                post.write(f"{cat},{cat_sum[cat]}\n")