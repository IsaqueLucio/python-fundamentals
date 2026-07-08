class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        return f"{self.title} by {self.author}."