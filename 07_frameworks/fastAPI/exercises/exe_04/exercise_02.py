"""
Exercise 2: Field validation constraints

Goal:
    Practice adding extra validation rules to Pydantic fields using
    Field(), beyond just the type itself.

Instructions:
    1. Create the FastAPI app instance.
    2. Define a Pydantic model `Movie` with fields:
       - title: str, using Field(..., min_length=1, max_length=100)
       - year: int, using Field(..., ge=1888, le=2100)
         (1888 is roughly when the first films were made — a fun
         real-world constraint to use here)
       - rating: float, using Field(..., ge=0.0, le=10.0)
    3. Create a module-level list called `movies` (starts empty).
    4. Create a POST "/movies" endpoint that:
       - receives a `Movie` in the request body
       - adds an "id" field (len(movies) + 1)
       - appends it to `movies`
       - returns the created dict

Run it with:
    uvicorn exercise_02:app --reload

Test in http://127.0.0.1:8000/docs:
    POST /movies
    Body: {"title": "Interstellar", "year": 2014, "rating": 9.5}
    -> should work

    POST /movies
    Body: {"title": "", "year": 2014, "rating": 9.5}
    -> should return 422 (title too short)

    POST /movies
    Body: {"title": "Old Film", "year": 1800, "rating": 9.5}
    -> should return 422 (year below minimum)

    POST /movies
    Body: {"title": "Bad Rating", "year": 2020, "rating": 15}
    -> should return 422 (rating above maximum)
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 2 - Field validation constraints",
    description="Practice adding extra validation rules to Pydantic fields using Field(), beyond just the type itself.",
    version="0.1.0",
)

# TODO: define the Movie Pydantic model with Field() constraints
# title: str (min_length=1, max_length=100)
# year: int (ge=1888, le=2100)
# rating: float (ge=0.0, le=10.0)
class Movie(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1888, le=2100)
    rating: float = Field(ge=0.0, le=10.0)

# TODO: create the `movies` list (starts empty)
movies: list[dict] = []

# TODO: POST "/movies" endpoint receiving a Movie body
# add an "id" field and append it to `movies`, then return it
@app.post("/movies")
def post_movies(movie: Movie):
    new_movie = movie.model_dump()
    new_movie["id"] = len(movies) + 1
    movies.append(new_movie)
    return new_movie
