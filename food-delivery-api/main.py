from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

# ------------------ DATA ------------------

foods = [
    {"id": 1, "name": "Pizza", "price": 250, "category": "Fast Food"},
    {"id": 2, "name": "Burger", "price": 120, "category": "Fast Food"},
    {"id": 3, "name": "Biryani", "price": 200, "category": "Main Course"},
]

cart = []
orders = []

# ------------------ MODELS ------------------

class Food(BaseModel):
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    category: str

class CartItem(BaseModel):
    food_id: int
    quantity: int = Field(..., gt=0, le=10)

class Order(BaseModel):
    customer_name: str = Field(..., min_length=2)
    address: str

# ------------------ HELPER FUNCTIONS ------------------

def find_food(food_id: int):
    for food in foods:
        if food["id"] == food_id:
            return food
    return None

def calculate_total():
    total = 0
    for item in cart:
        food = find_food(item["food_id"])
        total += food["price"] * item["quantity"]
    return total

# ------------------ DAY 1-2 APIs ------------------

@app.get("/")
def home():
    return {"message": "Welcome to Food Delivery API"}

@app.get("/foods")
def get_all_foods():
    return foods

@app.get("/foods/{food_id}")
def get_food(food_id: int):
    food = find_food(food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@app.get("/foods-summary")
def summary():
    return {"total_foods": len(foods)}

# ------------------ DAY 3 POST ------------------

@app.post("/foods", status_code=201)
def add_food(food: Food):
    new_food = {
        "id": len(foods) + 1,
        **food.dict()
    }
    foods.append(new_food)
    return new_food

@app.post("/cart")
def add_to_cart(item: CartItem):
    if not find_food(item.food_id):
        raise HTTPException(status_code=404, detail="Food not found")

    cart.append(item.dict())
    return {"message": "Added to cart"}

# ------------------ DAY 4 CRUD ------------------

@app.put("/foods/{food_id}")
def update_food(food_id: int, updated: Food):
    food = find_food(food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    food.update(updated.dict())
    return food

@app.delete("/foods/{food_id}")
def delete_food(food_id: int):
    food = find_food(food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    foods.remove(food)
    return {"message": "Food deleted"}

# ------------------ DAY 5 WORKFLOW ------------------

@app.get("/cart")
def view_cart():
    return cart

@app.post("/order")
def place_order(order: Order):
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = calculate_total()

    new_order = {
        "id": len(orders) + 1,
        "customer": order.customer_name,
        "address": order.address,
        "items": cart.copy(),
        "total": total,
        "status": "Placed"
    }

    orders.append(new_order)
    cart.clear()

    return new_order

@app.put("/order/{order_id}/deliver")
def deliver_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "Delivered"
            return order

    raise HTTPException(status_code=404, detail="Order not found")

# ------------------ DAY 6 ADVANCED ------------------

@app.get("/foods/search")
def search_food(keyword: Optional[str] = None):
    if keyword:
        return [f for f in foods if keyword.lower() in f["name"].lower()]
    return foods

@app.get("/foods/browse")
def browse_foods(
    keyword: Optional[str] = None,
    sort_by: str = "price",
    order: str = "asc",
    page: int = 1,
    limit: int = 2
):
    results = foods

    # Search
    if keyword:
        results = [f for f in results if keyword.lower() in f["name"].lower()]

    # Sort
    reverse = order == "desc"
    results = sorted(results, key=lambda x: x[sort_by], reverse=reverse)

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "total": len(results),
        "page": page,
        "data": results[start:end]
    }