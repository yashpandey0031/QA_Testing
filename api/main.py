from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Pydantic model: only describes and validates the shape of data in transit. Nothing is saved.
class Employee(BaseModel):
    name: str
    salary: int = 0

#data storage
employees = [
    {"id": 1, "name": "Yash", "salary": 40000},
    {"id": 2, "name": "Rahul", "salary": 50000},
]

# READ all 
@app.get("/employees")
def get_all():
    return employees

# READ one
@app.get("/employees/{emp_id}")
def get_one(emp_id: int):
    for e in employees:
        if e["id"] == emp_id:
            return e
    raise HTTPException(status_code=404, detail="Not found")

# CREATE
@app.post("/employees", status_code=201)
def create(emp: Employee):
    new = {"id": len(employees) + 1, **emp.model_dump()}
    employees.append(new)
    return new

# UPDATE
@app.put("/employees/{emp_id}")
def update(emp_id: int, emp: Employee):
    for e in employees:
        if e["id"] == emp_id:
            e.update(emp.model_dump())
            return e
    raise HTTPException(status_code=404, detail="Not found")

# DELETE
@app.delete("/employees/{emp_id}")
def delete(emp_id: int):
    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found")