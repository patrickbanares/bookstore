from fastapi import APIRouter

from .books.router import router as books_router
from .cart.router import router as cart_router

api_router = APIRouter()
api_router.include_router(books_router)
api_router.include_router(cart_router)
