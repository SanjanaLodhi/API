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


