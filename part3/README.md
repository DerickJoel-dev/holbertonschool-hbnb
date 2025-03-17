# 🏡 HBnB - Part 3: Authentication, Authorization, and Database Integration

In this phase of the **HBnB Project**, we have enhanced the application by implementing **secure user authentication**, **role-based authorization**, and **database integration** using **SQLAlchemy**. This upgrade improves **security**, **data consistency**, and **performance**.

---

## 🚀 New Features

### 🔐 **Authentication & Security**
- **Password hashing** using `Flask-Bcrypt`
- **JWT-based authentication** with `Flask-JWT-Extended`
- **Role-based access control (RBAC)**
- **Secure login/logout endpoints** with token generation
- **Protected API endpoints** with authorization checks

### 🗄️ **Database Integration**
- **SQLAlchemy ORM implementation**
- **Entity mapping** (`User`, `Place`, `Review`, `Amenity`)
- **Relationship management** between entities (`One-to-Many`, `Many-to-Many`)
- **MariaDB/MySQL database** for production
- **SQLite database** for development/testing

---

## 📋 Requirements
To run this project, ensure you have the following dependencies installed:

```bash
flask
flask-restx
flask-bcrypt
flask-jwt-extended
sqlalchemy
flask-sqlalchemy
pymysql
flask-migrate
```
## 🛠️ Installation & Setup
**1️⃣ Clone the repository:**
``` bash
git clone https://github.com/your-repo/hbnb.git
cd hbnb
```
## 2️⃣ Create and activate a virtual environment:
``` bash
python3 -m venv .env
source .env/bin/activate
```
## 3️⃣ Install dependencies:
``` bash
pip install -r requirements.txt
```
## 4️⃣ Set up environment variables:
``` bash
Create a .env file with the database configuration.
```
## 5️⃣ Initialize the database:
``` bash
flask db upgrade
```
## 6️⃣ Run the application:
``` bash
flask run
```
**The API will be available at: http://127.0.0.1:5000/api/v1/**
---
## 📡 API Endpoints

### 🌍 Public Endpoints
| Method | Endpoint                      | Description         |
|--------|--------------------------------|---------------------|
| `GET`  | `/api/v1/places/`             | List all places    |
| `GET`  | `/api/v1/places/<place_id>`    | Get place details  |

### 🔐 Protected Endpoints (Requires Authentication)
| Method   | Endpoint                      | Description                  |
|----------|--------------------------------|------------------------------|
| `POST`   | `/api/v1/places/`             | Create a new place           |
| `PUT`    | `/api/v1/places/<place_id>`    | Update place (owner only)    |
| `POST`   | `/api/v1/reviews/`            | Create a review              |
| `PUT`    | `/api/v1/reviews/<review_id>`  | Update review (author only)  |
| `DELETE` | `/api/v1/reviews/<review_id>`  | Delete review (author only)  |
| `PUT`    | `/api/v1/users/<user_id>`      | Update user profile (self only) |

### 🛑 Admin-Only Endpoints
| Method  | Endpoint                          | Description               |
|---------|----------------------------------|---------------------------|
| `POST`  | `/api/v1/users/`                 | Create new users         |
| `PUT`   | `/api/v1/users/<user_id>`        | Modify any user's details |
| `POST`  | `/api/v1/amenities/`             | Add new amenities        |
| `PUT`   | `/api/v1/amenities/<amenity_id>` | Modify amenities         |


## 🔑 Authentication
To access protected endpoints, include the JWT token in the Authorization header:

``` bash
Authorization: Bearer <your_jwt_token>
```
**Example login request:**
``` bash
curl -X POST "http://127.0.0.1:5000/api/v1/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "email": "test@example.com",
  "password": "mypassword"
}'
```
**Example response:**
``` bash
{
  "access_token": "your_generated_jwt_token"
}
```
## 🗃️ Database Schema
**This project uses a relational database with the following tables:**

- **Users** (`id`, `first_name`, `last_name`, `email`, `password`, `is_admin`)
- **Places** (`id`, `name`, `description`, `price`, `latitude`, `longitude`, `owner_id`)
- **Reviews** (`id`, `text`, `rating`, `user_id`, `place_id`)
- **Amenities** (`id`, `name`)
- **Place_Amenity** (Many-to-Many relation between `places` and `amenities`)
---

## Authors

- [@DerickJoel-dev](https://github.com/DerickJoel-dev)