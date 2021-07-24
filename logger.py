from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
file_name = "api-log"
log_file = open(file_name, "a")


class Item(BaseModel):
    text: str


@app.get("/")
def read_log():
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return {"log": lines}


@app.post("/")
def write_log(item: Item):
    log_file.write(str(item.text) + "\n")
    log_file.flush()
    return {"Message": "Success"}
