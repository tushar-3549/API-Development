# 📱 Social Media API

A high-performance Social Media API built using **FastAPI**, **PostgreSQL**, and **Alembic**. This project implements secure user authentication, robust database operations, and thorough testing to ensure a reliable and efficient system.

---

## 🚀 Features

- 🔐 **User Authentication** (JWT-based login/logout using OAuth2)
- 📝 **CRUD Operations** for posts and users
- 🔑 **Password Hashing** for secure login credentials
- 🗄️ **PostgreSQL Integration** using SQLAlchemy ORM
- 🔄 **Alembic Migrations** for schema versioning
- 🛡️ **SQL Injection Prevention** with ORM best practices
- ✅ **Unit Testing** with Pytest (users, auth, DB, API endpoints)
- 🧪 **Postman API Testing** support
- ⚙️ **GitHub Actions** for CI/CD

---

## 🛠️ Technologies Used

- **FastAPI** – Modern, high-performance web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for interacting with the DB
- **Alembic** – Database migrations
- **OAuth2 & JWT** – Secure authentication
- **Pytest** – Python testing framework
- **GitHub Actions** – CI/CD automation

---

## 📦 Installation

### ✅ Prerequisites

Ensure the following are installed:

- Python (3.10 or higher)
- PostgreSQL
- Virtual environment module (venv)

### 🔧 Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tushar-3549/API-Development.git
   cd API-Development
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   `pip install -r requirements.txt`
4. **Set up your `.env` file**
   ```
   DATABASE_URL=postgresql://<username>:<password>@localhost/<dbname>
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
5. **Apply Alembic migrations**
   `alembic upgrade head`
6. **Run the FastAPI server**
   `uvicorn app.main:app --reload`
- Visit the API at: `http://127.0.0.1:8000`
- Docs: `http://127.0.0.1:8000/docs`
- 🧪 **Running Tests**
  ```pytest```

