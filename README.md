# 🍔 Food Delivery FastAPI Backend

## 📌 Project Description

This project is a fully functional backend system built using **FastAPI** as part of the FastAPI Internship Final Project.

The application simulates a real-world **Food Delivery System**, allowing users to browse food items, add them to a cart, place orders, and track delivery status. It demonstrates REST API development, data validation, and backend workflow design.

---

## 🚀 Features

### ✅ Basic APIs (Day 1–2)

* Home route (`/`)
* Get all food items (`/foods`)
* Get food by ID (`/foods/{id}`)
* Summary endpoint (`/foods-summary`)

### ✅ POST APIs with Validation (Day 3)

* Add new food item with Pydantic validation
* Add items to cart with quantity constraints
* Proper error handling using HTTP status codes

### ✅ CRUD Operations (Day 4)

* Create food item
* Update food item
* Delete food item
* Handles:

  * `201 Created`
  * `404 Not Found`

### ✅ Multi-Step Workflow (Day 5)

* Cart → Order → Delivery process:

  1. Add items to cart
  2. Place order
  3. Mark order as delivered

### ✅ Advanced APIs (Day 6)

* Keyword-based search (`/foods/search`)
* Sorting (price-based)
* Pagination support
* Combined browsing endpoint (`/foods/browse`)

---

## 🛠️ Tech Stack

* **FastAPI**
* **Python**
* **Pydantic**
* **Uvicorn**

---

## 📂 Project Structure

food-delivery-api/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run Server

```
uvicorn main:app --reload
```

### 3️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📸 API Testing (Screenshots)

All endpoints are tested using Swagger UI.

Example screenshots included:

* Home route
* Get all foods
* Get food by ID
* Add food
* Add to cart
* Place order
* Deliver order
* Search API
* Browse API (Search + Sort + Pagination)

---

## 🔄 Workflow Explanation

1. User browses food items
2. Adds items to cart
3. Places an order
4. Order is processed and marked as delivered

---

## ⚠️ Error Handling

* 400 → Bad Request (e.g., empty cart)
* 404 → Not Found (invalid food/order ID)
* Validation errors handled using Pydantic

---

## 💡 Key Learnings

* FastAPI routing and structure
* Request validation using Pydantic
* CRUD operations
* API design and best practices
* Real-world workflow implementation
* Query parameters (search, sort, pagination)

---

## 📌 Future Improvements

* Add database (MongoDB / PostgreSQL)
* Implement authentication (JWT)
* Add payment integration
* Deploy using Docker / Cloud

---

## 👨‍💻 Author

Rushikesh Hadawale

---

## ⭐ Conclusion

This project demonstrates the ability to build scalable and structured backend APIs using FastAPI, covering all concepts from basic routing to advanced API features.
