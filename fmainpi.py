from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Employee(BaseModel):
    name:str
    role:str

employee = {
    1:{
        "name": "Ganesh",
        "role": "Tester"
    },
    2: {
           "name": "shaik",
           "role": "si"
    },
    3: {
           "name": "ik",
           "role": "ci"
       }
}
@app.get("/test/{employee_id}")
def test(employee_id:int):
    if employee_id in employee:
        return employee[employee_id]
    return {"error": "details not found"}
@app.get("/basic")
def test():
    return{"Test":"Manual input"}
@app.post("/post/{employe_id}")
def create(employe_id: int, employe: Employee):
    if employe_id in employee:
        return {"Employee": "ID already exists"}
    employee[employe_id] = employe
    return employee[employe_id]

@app.put("/update/{employe_id}")
def update(employe_id:int, employe:Employee):
    if employe_id not in employee:
        return {"Employe": "NOt exsists"}
    employee[employe_id] = employe
    return employee[employe_id]

@app.delete("/delete/{employe_id}")
def delete_employee(employe_id:int):
    if employe_id not in employee:
        return {"Error":"not exists"}
    del employee[employe_id]
    return {"employee":"Deleted"}