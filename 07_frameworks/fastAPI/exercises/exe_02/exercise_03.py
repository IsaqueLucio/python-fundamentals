"""
Exercise 3: Combining path + query params (and route ordering)

Goal:
    Build a slightly bigger example combining path params, query
    params, and a fixed in-memory list, while practicing the route
    ordering rule from the previous topic.

Instructions:
    1. Create the FastAPI app instance.
    2. Create a module-level list called `employees` with at least 4
       dicts, each with "id" (int), "name" (str), and "department" (str).
    3. Create a GET "/employees/search" endpoint with an optional query
       param `department` (str, default None). If department is provided,
       return only employees matching it; otherwise return all employees.
       IMPORTANT: this route must be declared BEFORE the one below,
       otherwise "search" would be captured as {employee_id} and fail
       the int conversion.
    4. Create a GET "/employees/{employee_id}" endpoint (employee_id: int)
       that searches `employees` for a matching "id" and returns it.
       If no employee is found, return {"error": "Employee not found"}
       with status_code=404 (you don't need exception handling yet,
       just return the dict with the right status code).

Run it with:
    uvicorn exercise_3:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /employees/search                     -> all employees
    - GET /employees/search?department=Backend  -> filtered list
    - GET /employees/1                           -> single employee
    - GET /employees/999                         -> 404 error dict
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse


# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 3 - Combining path + query params (and route ordering)",
    description='''
    Build a slightly bigger example combining path params, 
    query params, and a fixed in-memory list, 
    while practicing the route ordering rule from the previous topic. ''',
    version="0.1.0",
)

# TODO: create the `employees` list with at least 4 sample employees
# each with "id", "name", "department"
employees = [
    {"id": 1, "name": "Alice", "department": "Engineering"},
    {"id": 2, "name": "Bob", "department": "Marketing"},
    {"id": 3, "name": "Carol", "department": "Finance"},
    {"id": 4, "name": "David", "department": "Human Resources"},
]

# TODO: GET "/employees/search" endpoint
# optional query param: department (str, default None)
# must be declared BEFORE "/employees/{employee_id}"
@app.get("/employees/search")
def get_employees_department(department: str = None):
    if department is not None:
        temp = []
        for employee in employees:
            if employee["department"] == department:
                temp.append(employee)
        return {f"employees_{department}": temp}
    
    return {"employees": employees}

# TODO: GET "/employees/{employee_id}" endpoint (employee_id: int)
# return the matching employee, or {"error": "Employee not found"}
# with status_code=404 if none matches
@app.get("/employees/{employee_id}")
def get_employees_id(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return {"employee_with_id": employee}
    return JSONResponse(
        status_code=404,
        content={"error": "Employee not found"}
    )