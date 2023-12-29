from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(text: str = "world"):
    return {"Hello": text}
