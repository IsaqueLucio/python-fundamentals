"""
Exercise 3: Combining response_model with status_code, and
response_model_exclude as a shortcut

Goal:
    Practice two extra tools that pair naturally with response_model:
    - setting a custom success status_code (e.g. 201 Created for POST)
    - using response_model_exclude as a quick way to hide fields
      WITHOUT declaring a whole separate output model (useful for
      quick internal tools, though separate models are usually
      preferred for public APIs).

Instructions:
    1. Create the FastAPI app instance.
    2. Define a single Pydantic model `Employee` with fields:
       - id: int
       - name: str
       - department: str
       - salary: float
    3. Create a module-level list called `employees` (starts empty).
    4. Create a POST "/employees" endpoint that:
       - receives name, department, and salary directly as a request
         body using the Employee model (you'll need to accept an
         Employee where the client doesn't send "id" -- for THIS
         exercise, simplify by declaring a separate `EmployeeCreate`
         model without the id field, same pattern as previous topics)
       - response_model=Employee
       - status_code=201 (set this directly in the decorator, e.g.
         @app.post("/employees", response_model=Employee, status_code=201))
       - builds the full dict (with id) and appends it to `employees`
    5. Create a GET "/employees/{employee_id}" endpoint that:
       - response_model=Employee
       - response_model_exclude={"salary"}  (a set of field names to
         hide from the response, without needing a separate model)
       - finds and returns the matching employee, or raises
         HTTPException(404, "Employee not found")

Run it with:
    uvicorn exercise_03:app --reload

Test in http://127.0.0.1:8000/docs:
    POST /employees
    Body: {"name": "Carol", "department": "Finance", "salary": 8000}
    -> should return with status code 201, INCLUDING salary (this is
       the "internal" creation response, e.g. for an HR admin tool)

    GET /employees/1
    -> should return WITHOUT the salary field (e.g. for a public
       employee directory endpoint)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 3 - Combining response_model with status_code, and response_model_exclude as a shortcut",
    description= """
      Practice two extra tools that pair naturally with response_model:
      - setting a custom success status_code (e.g. 201 Created for POST)
      - using response_model_exclude as a quick way to hide fields
        WITHOUT declaring a whole separate output model (useful for
        quick internal tools, though separate models are usually
        preferred for public APIs).
    """,
    version="0.1.0",
)

# TODO: define EmployeeCreate (input model, no id)
# fields: name (str), department (str), salary (float)
class EmployeeCreate(BaseModel):
    name: str
    departament: str
    salary: float

# TODO: define Employee (full model, includes id)
# fields: id (int), name (str), department (str), salary (float)
class Employee(BaseModel):
    id: int
    name: str
    departament: str
    salary: float

# TODO: create the `employees` list (starts empty)
employees: list[dict] = []

# TODO: POST "/employees" endpoint
# response_model=Employee, status_code=201
@app.post("/employees", response_model=Employee, status_code=201)
def post_employees(employee: EmployeeCreate):
    new_employee = employee.model_dump()
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return new_employee

# TODO: GET "/employees/{employee_id}" endpoint
# response_model=Employee, response_model_exclude={"salary"}
# raise HTTPException(404, "Employee not found") if missing
@app.get("/employees/{employee_id}", response_model=Employee, response_model_exclude={"salary"})
def get_per_employee(employee_id: int):
  for employee in employees:
      if employee["id"] == employee_id:
          return employee
  raise HTTPException (status_code=404, detail="Employee not found")