# 📱 iPhone Sales Tracker API – FastAPI (Single File Version)

A FastAPI-based REST API to track iPhone sales for a retail chain. This simple CRUD application handles basic sales operations and provides basic analytics.

---

## 🚀 Tech Stack

- **Python** 3.8+
- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **psycopg2-binary**
- **Pydantic**

---
# iPhone Sales Tracker API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📌 Table of Contents
- [Features](#-features)
- [Setup](#-setup-instructions)
- [API Reference](#-api-reference)
  - [Endpoints](#-api-endpoints)
  - [Examples](#-api-examples)
- [Design Decisions](#-design-decisions)
- [Testing](#-testing)
- [Project Structure](#-project-structure)

## 🚀 Features
- CRUD operations for iPhone sales
- Sales statistics dashboard
- Filterable sales data
- PostgreSQL backed with data validation

## 🛠️ Setup Instructions
_(Previous setup content remains unchanged...)_

## 📡 API Reference

### 🔌 Endpoints
| Endpoint          | Method | Description                      |
|-------------------|--------|----------------------------------|
| `/sales`          | POST   | Create new sale record           |
| `/sales`          | GET    | List all sales (filterable)      |
| `/sales/{id}`     | GET    | Get specific sale               |
| `/sales/{id}`     | PUT    | Update sale record               |
| `/sales/{id}`     | DELETE | Delete sale record               |
| `/sales/stats`    | GET    | Get sales statistics            |

### 💡 API Examples

**1. Create Sale**
```bash
POST /sales
## 🏗️ PostgreSQL Table Schema

Create this table before starting the app:

```sql
CREATE TABLE iphone_sales (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone_model VARCHAR(50) NOT NULL,
    color VARCHAR(30) NOT NULL,
    storage_gb INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    sale_date DATE NOT NULL,
    store_location VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



