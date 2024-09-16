from fastapi import APIRouter
from .model import CartItem
from fastapi.exceptions import HTTPException
from app.utils import load_data, save_data


router = APIRouter(
    tags=['Cart'],
    prefix='/cart'
)

CART_FILE = 'app/cart.json'

# add to cart
@router.post("/cart", status_code=201)
def add_to_cart(item: CartItem):
    cart = load_data(CART_FILE)
    for cart_item in cart:
        if cart_item['book_id'] == item.book_id:
            cart_item['quantity'] += item.quantity
            save_data(CART_FILE, cart)
            return {"message": "Updated cart item quantity."}
    cart.append(item.model_dump())
    save_data(CART_FILE, cart)
    return {"message": "Added book to cart."}

# remove from cart
@router.delete("/cart/{book_id}", status_code=204)
def delete_from_cart(book_id: int):
    cart = load_data(CART_FILE)
    updated_cart = [item for item in cart if item['book_id'] != book_id]
    save_data(CART_FILE, updated_cart)
    return {"message": "Removed item from cart."}

# update cart
@router.put("/cart", status_code=200)
def update_cart(item: CartItem):
    cart = load_data(CART_FILE)
    for cart_item in cart:
        if cart_item['book_id'] == item.book_id:
            cart_item['quantity'] = item.quantity
            save_data(CART_FILE, cart)
            return {"message": "Updated cart item."}
    raise HTTPException(status_code=404, detail="Item not found.")

# checkout
@router.post("/checkout", status_code=200)
def checkout():
    cart = load_data(CART_FILE)
    if len(cart)==0:
        return {"message": "Cart is empty, nothing to checkout"}
    save_data(CART_FILE, [])
    return {"message": "Checkout successful, cart is cleared."}