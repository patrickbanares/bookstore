from fastapi import APIRouter
from app.utils import load_data, save_data
from typing import List
from .model import Book

BOOKS_FILE = "app/books.json"

router = APIRouter(
    tags=['books'],
    prefix='/books'
)

@router.get("", response_model=List[Book])
def get_books():
    books = load_data(BOOKS_FILE)
    return books