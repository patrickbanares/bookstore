from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import api_router

app_configs = {
    "title": "Bookstore",
    "description": "",
    "version": "0.0.1",
    "root_path": "/",
}

app = FastAPI(**app_configs)

BOOKS_FILE = "books.json"
CART_FILE = "cart.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return "App is running and working!!"

app.include_router(api_router)

