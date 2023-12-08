from fastapi import FastAPI
from pydantic import BaseModel
from calculator import addition, multiplication,division,substraction

class User_Input(BaseModel):
    value_1 : float
    value_2 : float

app = FastAPI()

@app.post("/addition")
def add(input:User_Input):
    result = addition(input.value_1,input.value_2)
    return result

@app.post("/substraction")
def subtract(input:User_Input):
    result = substraction(input.value_1,input.value_2)
    return result

@app.post("/multiplication")
def multiply(input:User_Input):
    result = multiplication(input.value_1,input.value_2)
    return result

@app.post("/division")
def divide(input:User_Input):
    result = division(input.value_1,input.value_2)
    return result





