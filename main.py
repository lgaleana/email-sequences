from fastapi import FastAPI
from models import EmailSchedule

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}