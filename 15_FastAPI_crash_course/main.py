from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    # using help of pydantic
    id: int
    name: str
    origin: str

# teas will hold data of Tea
teas: List[Tea] = []

# decorator and then its function(method)
@app.get("/")
def read_root():
    return {"message": "Welcome to my tea house"}

# get teas
@app.get("/teas")
def get_teas():
    return teas

# add new tea
@app.post("/teas")
def add_tea(tea: Tea): # tea: Tea (here Tea is for validation means these (fields) must be added here)
    teas.append(tea)
    return tea

# update tea
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found error!!"}

# delete tea
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"error": "Tea not found error!!"}