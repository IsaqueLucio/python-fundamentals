"""
Exercise 3: A tiny "in-memory API"

Goal:
    Combine what you learned into a slightly more realistic endpoint,
    without path/query params yet (that's the next topic).

Instructions:
    1. Create the FastAPI app instance.
    2. Create a module-level list called `tasks` with a few dicts inside,
       e.g. [{"id": 1, "title": "Learn FastAPI", "done": False}, ...].
       (This simulates a "database" for now — no real DB yet.)
    3. Create a GET "/tasks" endpoint that returns the full `tasks` list.
    4. Create a GET "/tasks/count" endpoint that returns
       {"total": <number of tasks>}.

       Careful: route order matters in FastAPI! If you later add a route
       like "/tasks/{task_id}", it must come AFTER "/tasks/count",
       otherwise FastAPI will try to match "count" as a task_id.
       For this exercise you don't need "/tasks/{task_id}" yet — just
       keep this rule in mind for the next topic.

Run it with:
    uvicorn exercise_3:app --reload

Check both routes in http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Exercise 3: A tiny in-memory API",
    description="Combine what you learned into a slightly more realistic endpoint, without path/query params yet (that's the next topic).",
    version="0.1.0",
)

# TODO: create the `tasks` list with at least 3 sample tasks
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build an API", "done": False},
    {"id": 3, "title": "Practice endpoints", "done": True},
]

# TODO: GET "/tasks" endpoint returning the full list
@app.get("/tasks")
def get_tasks():
    return tasks

# TODO: GET "/tasks/count" endpoint returning {"total": <n>}
@app.get("/tasks/count")
def get_tasks_count():
    return {"total": len(tasks)}