"""
Exercise 2: Multiple endpoints + status codes

Goal:
    Practice creating more than one route and controlling the HTTP
    status code returned, similar to using ResponseEntity in Spring.

Instructions:
    1. Create the FastAPI app instance.
    2. Create a GET "/about" endpoint that returns a dict describing
       this learning module, e.g. {"module": "FastAPI basics", "week": 1}.
    3. Create a GET "/ping" endpoint that returns {"pong": True} with
       an explicit 200 status code, using the `status_code` parameter
       of the route decorator (@app.get("/ping", status_code=200)).
    4. Create a GET "/not-found-example" endpoint that returns a dict
       but with status_code=404, just to see how it behaves in /docs.

Run it with:
    uvicorn exercise_2:app --reload

Check all three routes manually in http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Exercise 2: Multiple endpoints + status codes",
    description="Practice creating more than one route and controlling the HTTP status code returned, similar to using ResponseEntity in Spring.",
    version="0.1.0",
)
# TODO: GET "/about" endpoint
@app.get("/about")
def get_about():
    return {
        "module": "FastAPI basics", 
        "week": 1
        }
# TODO: GET "/ping" endpoint with explicit status_code=200
@app.get("/ping", status_code=200)
def get_ping():

    return {"pong": True}
# TODO: GET "/not-found-example" endpoint with explicit status_code=404
@app.get("/not-found-example", status_code=404)
def get_not_found_example():
    return {"test": False}