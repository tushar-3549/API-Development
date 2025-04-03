### Social Media API
- A high-performance Social Media API built using FastAPI, PostgreSQL, and Alembic. This project implements user authentication, database operations, and testing to ensure a secure and efficient system.

### Features
- User Authentication (JWT-based login/logout using OAuth2)
- CRUD Operations for posts and users
- Password Hashing for secure authentication
- Database Integration with PostgreSQL & SQLAlchemy ORM
- Alembic Migrations for database schema management
- SQL Injection Prevention using ORM best practices
- Unit Testing with Pytest (Users, Database, Authentication, API endpoints)
- Postman API Testing support

### Technologies Used
- FastAPI - Modern web framework for APIs
- PostgreSQL - Relational database management system
- SQLAlchemy - ORM for database interaction
- Alembic - Database migration tool
- OAuth2 & JWT - Secure authentication
- Github Actions
- Pytest - Automated testing framework

### Installation
***Prerequisites***
Ensure you have the following installed:
- Python (3.10 or higher)
- PostgreSQL
- Virtual Environment (venv)

### Steps

**Clone the repository:**
```
git clone https://github.com/your-username/your-repo.git
cd API-Development
```

###### Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Start the FastAPI server:**

`uvicorn app.main:app --reload`

- API will be available at: `http://127.0.0.1:8000`
