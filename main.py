from fastapi import FastAPI
from mongoengine.queryset.visitor import Q
from models import Employee
from mongoengine import connect
import json
from fastapi import Path
from fastapi import Query
from pydantic import BaseModel
from fastapi import Body


app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get("/")
def home():
    return "Hello! It's my task"


@app.get("/all_employees")
def all_employees():
    employees = json.loads(Employee.objects().to_json())
    # print(employees)
    # employees_list = json.loads(employees)
    return {"employees": employees}


@app.get("/employee/{employee_id}")
def get_employee(employee_id: int = Path(..., gt=0)):
    employee = Employee.objects.get(employee_id=employee_id)

    employee_dict = {
        "employee_id": employee.employee_id,
        "name": employee.name,
        "email": employee.email,
        "age": employee.age,
        "company": employee.company,
        "join_date": employee.join_date,
        "job_title": employee.job_title,
        "gender": employee.gender,
        "salary": employee.salary
    }
    return employee_dict


@app.get("/search_employees")
def search_employees(name: str, age: int = Query(None, gt=18)):
    employees = json.loads(Employee.objects.filter(Q(name__icontains=name) | Q(age=age)).to_json())
    return {"employees": employees}


class NewEmployee(BaseModel):
    employee_id: int
    name: str
    email: str
    age: int = Body(None, gt=18)
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int


@app.post("/new_employee")
def add_employee(employee: NewEmployee):
    new_employee = Employee(employee_id=employee.employee_id,
                            name=employee.name,
                            email=employee.email,
                            age=employee.age,
                            company=employee.company,
                            join_date=employee.join_date,
                            job_title=employee.job_title,
                            gender=employee.gender,
                            salary=employee.salary
                            )

    new_employee.save()

    return {"message": "Employee added successfully!"}