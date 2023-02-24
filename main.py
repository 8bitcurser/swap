from fastapi import FastAPI

from src.supervielle import Supervielle

banks = {
    'supervielle': {
        "bank": Supervielle,
        "keys": ('supervielle', 'Concepto')
    }
}


app = FastAPI()


@app.get('/')
def read_root():
    return {"Status": "Astor 0.1"}

@app.get('/banks/{bank_name}/{client_cuil}')
def recat_supervielle(bank_name: str, client_cuil: int):
    bank = banks.get(bank_name)
    bank = bank['bank'](*bank['keys'], client_cuil)
    if bank:
        bank.recategorization()
        bank.post_processing('Débito', 'Crédito')
        bank.get_thirdparty_transfers()
        return {"Status": f"{bank_name} processed", "Client": f"{client_cuil}"}
    return {"Status": f"{bank_name} not supported"}
