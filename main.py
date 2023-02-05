from fastapi import FastAPI

from src.supervielle import supervielle


app = FastAPI()


@app.get('/')
def read_root():
    return {"Status": "Astor 0.1"}

@app.get('/banks/supervielle/recat')
def recat_supervielle():
    supervielle.recategorization()
    return {"Status": "Supervielle recat done"}

@app.get('/banks/supervielle/post')
def post_supervielle():
    supervielle.post_processing()
    return {"Status": "Supervielle post process done"}
