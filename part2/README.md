## 📌Part 2: Implementation of Business Logic and API Endpoints
- This project is a RESTful API for the HBNB platform, developed using Flask and Flask-RESTx. It handles multiple endpoints for managing users, places, amenities, and reviews. This phase focuses on testing and validation, ensuring the API works as expected.

## The API performs:
CRUD operations on various entities.
Validation checks for request data.
Automated and manual testing using **unittest** and **cURL**.

## 📂 Directory Structure
``` bash
📦 holbertonschool-hbnb/
 ├── part2/
 │   ├── hbnb/
 │   │   ├── app/
 │   │   │   ├── api/
 │   │   │   │   ├── v1/
 │   │   │   │   │   ├── amenities.py
 │   │   │   │   │   ├── places.py
 │   │   │   │   │   ├── reviews.py
 │   │   │   │   │   ├── users.py
 │   │   │   │   │   ├── __init__.py
 │   │   │   ├── services/
 │   │   │   │   ├── facade.py
 │   │   │   │   ├── repository.py
 │   │   │   │   ├── __init__.py
 │   │   │   ├── __init__.py
 │   │   ├── models/
 │   │   │   ├── base_model.py
 │   │   │   ├── amenity.py
 │   │   │   ├── place.py
 │   │   │   ├── review.py
 │   │   │   ├── user.py
 │   │   │   ├── __init__.py
 │   │   ├── tests/
 │   │   │   ├── test_amenities_endpoints.py
 │   │   │   ├── test_places_endpoints.py
 │   │   │   ├── test_reviews_endpoints.py
 │   │   │   ├── test_users_endpoints.py
 │   │   │   ├── test_base_model.py
 │   │   │   ├── __init__.py
 │   │   ├── requirements.txt
 │   │   ├── README.md
 ```
---
## 🚀 Installation


- **Clone this repository**
``` bash
git clone https://github.com/yourusername/holbertonschool-hbnb.git
```



## 📡 API Endpoints
- The API provides endpoints for:

- Users
- Places
- Amenities
- Reviews
---
## 🔹 Example cURL Commands

## 1️⃣ Create an Amenity
``` bash 
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Swimming Pool"}'
```

### ✅ Expected Response (201 Created)
``` bash
{
  "id": "test-uuid",
  "name": "Swimming Pool"
}
```
## 2️⃣ Retrieve All Places
``` bash
curl -X GET http://127.0.0.1:5000/api/v1/places/
``` 
## ✅ Expected Response (200 OK)
``` bash
[
  {
    "id": "place-123",
    "name": "Beach House",
    "city_id": "test-city-id"
  }
]
```
## 3️⃣ Create a User
``` bash 
curl -X POST http://127.0.0.1:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "securepass"}'
```
## ✅ Expected Response (201 Created)
``` bash
{
  "id": "user-uuid",
  "email": "test@example.com"
}
```
---
## 🧪 Automated Testing
- All endpoints are validated using **unittest**. To run all **tests**:


- python3 -m unittest discover tests/
## 🔹 Test Cases:

## ✅ test_amenities_endpoints.py
- GET /amenities → Retrieves all amenities
- POST /amenities → Creates a new amenity (valid & invalid cases)
## ✅ test_places_endpoints.py
- GET /places → Retrieves all places
- POST /places → Creates a new place (valid & invalid cases)
## ✅ test_reviews_endpoints.py
- GET /reviews → Retrieves all reviews
- POST /reviews → Creates a new review (valid & invalid cases)
## ✅ test_users_endpoints.py
- GET /users → Retrieves all users
- POST /users → Creates a new user (valid & invalid cases)

---
## 📝 Author
Derick Joel Quiñones Medina
Holberton School - Software Engineering Student
