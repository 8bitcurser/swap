from src.helpers import read_recat, convert_csv_to_xls

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
        file_name = f'post_process/{self.name}.csv'
        with open(file_name, 'w') as post:
            post.write("concepto,monto\n")
            for cat in cat_sum:
                post.write(f"{cat},{cat_sum[cat]}\n")
        
        convert_csv_to_xls(file_name, destination='post_process')