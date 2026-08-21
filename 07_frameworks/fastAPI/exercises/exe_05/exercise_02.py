"""
Exercise 2: response_model with a list endpoint

Goal:
    Practice using response_model=list[Model] for endpoints that
    return multiple items, combined with a nested model from the
    previous topic.

Instructions:
    1. Create the FastAPI app instance.
    2. Define a Pydantic model `Author` with fields:
       - name: str
       - country: str
    3. Define a Pydantic model `BookCreate` (input) with fields:
       - title: str
       - author: Author (nested)
       - internal_notes: str = ""  (an editor-only note, should never
         be exposed publicly)
    4. Define a Pydantic model `BookOut` (output) with fields:
       - id: int
       - title: str
       - author: Author
       (no internal_notes!)
    5. Create a module-level list called `books` (starts empty).
    6. Create a POST "/books" endpoint with response_model=BookOut that
       receives a BookCreate, builds a full dict (with id and
       internal_notes included), appends it to `books`, and returns it.
    7. Create a GET "/books" endpoint with response_model=list[BookOut]
       that returns the full `books` list (internal_notes gets
       stripped automatically for every item).

Run it with:
    uvicorn exercise_02:app --reload

Test in http://127.0.0.1:8000/docs:
    POST /books
    Body: {
      "title": "Dune",
      "author": {"name": "Frank Herbert", "country": "USA"},
      "internal_notes": "bestseller, reprint in Q3"
    }
    -> response should NOT include internal_notes

    GET /books
    -> should return a list, none of the items showing internal_notes
"""

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 1 - Hiding a sensitive field with response_model",
    description= """
      Practice using response_model=list[Model] for endpoints that
      return multiple items, combined with a nested model from the
      previous topic.
    """,
    version="0.1.0",
)

# TODO: define Author model
# fields: name (str), country (str)
class Author(BaseModel):
    name: str
    country: str

# TODO: define BookCreate (input model)
# fields: title (str), author (Author), internal_notes (str = "")
class BookCreate(BaseModel):
    title: str
    author: Author
    internal_notes: str = ""

# TODO: define BookOut (output model)
# fields: id (int), title (str), author (Author) -- no internal_notes!
class BookOut(BaseModel):
    id: int
    title: str
    author: Author

# TODO: create the `books` list (starts empty)
books: list[dict] = []

# TODO: POST "/books" endpoint with response_model=BookOut
@app.post("/books", response_model=BookOut)
def post_books(book: BookCreate):
   new_book = {
      "id": len(books) + 1,
      "title": book.title,
      "author": book.author,
      "internal_notes": book.internal_notes
   }
   books.append(new_book)
   return new_book

# TODO: GET "/books" endpoint with response_model=list[BookOut]
@app.get("/books", response_model=list[BookOut])
def get_books():
    return books
