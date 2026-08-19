"""
Exercise 1: Create your first endpoint

Goal:
    Create a FastAPI app with a single GET endpoint at "/" that returns
    a JSON object with your name and your current role.

Instructions:
    1. Import FastAPI and create an app instance.
    2. Define a GET endpoint at "/".
    3. Return a dict with the keys "name" and "role".
       Example: {"name": "Isaque", "role": "Backend Developer"}

Run it with:
    uvicorn exercise_1:app --reload

Then check the result at:
    http://127.0.0.1:8000
"""

from fastapi import FastAPI

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Exercise 1: Create your first endpoint",
    description="First endpoint exercise for the python-fundamentals repo",
    version="0.1.0",
)

# TODO: define the GET "/" endpoint that returns a dict
# with "name" and "role" keys
@app.get("/")
def basic_get_exercise():
    '''
    Root for exercise 01 about FastAPI
    '''
    return {
        "username": "Todd",
        "role": "Backend Developer",
        "age": 20
    }