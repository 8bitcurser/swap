from src.helpers import read_extract, read_recat, convert_csv_to_xls

class Bank:
    def __init__(self, name, key, cuil):
        self.name = name
        self.key = key
        self.cuil = cuil

    def recategorization(self):
        """
        nombre banco
            fecha | codigo | concepto | debito | credito | saldo
        """
        pass
    
    def post_processing(self, debit_key, credit_key):
        # TODO: Do it based on bank categories not astor ones
        cat_sum = {}
        data = read_extract(f'{self.name}')
        for record in data:
            concepto = record[self.key]
            monto = record[credit_key] if not record[debit_key] else record[debit_key]
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
    
    def get_thirdparty_transfers(self):
        data = read_recat(f"{self.name}.csv")
        transfers = [
            line for line in data if line['codigo'] == '12' and line['objetivo'] != self.cuil and line['debito']]
        transfers_by_cuil = {
        }
        for transfer in transfers:
            thirdparty_cuil = transfer['objetivo']
            monto = transfer['debito']
            monto = float(monto.replace('.', '').replace(',', '.'))
            if transfers_by_cuil.get(thirdparty_cuil) is not None:
                transfers_by_cuil[thirdparty_cuil] += monto
            else:
                transfers_by_cuil[thirdparty_cuil] = monto
        file_name = f'transfers/{self.name}.csv'
        with open(file_name, 'w') as post:
            post.write("cuil,monto\n")
            for transfer in transfers_by_cuil:
                post.write(f"{transfer},{'{:.2f}'.format(transfers_by_cuil[transfer])}\n")
        
        convert_csv_to_xls(file_name, destination='transfers')