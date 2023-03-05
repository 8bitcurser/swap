from fastapi import FastAPI

from src.supervielle import Supervielle

banks = {
    'supervielle': Supervielle
}


app = FastAPI()


@app.get('/')
def read_root():
    return {"Status": "Astor 0.1"}

@app.get('/banks/{bank_name}/{client_cuil}')
def process(bank_name: str, client_cuil: int):
    bank = banks.get(bank_name)
    bank.cuil = client_cuil
    if bank:
        bank.load()
        return {
            "Status": f"{bank_name} processed",
            "Client": f"{client_cuil}"
        }
    return {"Status": f"{bank_name} not supported"}
