# Share Thoughts API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

A modern, high-performance Social Media API backend built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This API supports secure authentication, real-time voting, nested comments, and seamless deployment.

---

## 🚀 Features

- **Secure Authentication**: OAuth2 with JWT (Access & Refresh tokens).
- **Post Management**: Full CRUD operations for user posts.
- **Commenting System**: Add and retrieve comments for any post.
- **Dynamic Voting**: Smart vote toggling (Like/Unlike) and vote counts.
- **User Profiles**: Dedicated endpoints for user registration and profile management.
- **Database Versioning**: Automated migrations with Alembic.
- **Safety First**: Built-in protection against SQL Injection using SQLAlchemy ORM.
- **System Health**: Real-time health check endpoint for API and Database status.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Auth**: [JOSE](https://python-jose.readthedocs.io/) & [Passlib](https://passlib.readthedocs.io/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 🏁 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL installed and running

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tushar-3549/API-Development.git
   cd API-Development
   ```

2. **Setup virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_NAME=social_media
   DATABASE_USERNAME=postgres
   DATABASE_PASSWORD=your_password
   SECRET_KEY=your_secure_random_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run Migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the Server**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📖 API Documentation

Once the server is running, you can access the interactive Swagger UI at:
- **Local**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Primary Endpoints

| Category | Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- | :---: |
| **Auth** | `POST` | `/login` | User login & get tokens | No |
| | `POST` | `/auth/refresh` | Refresh access token | Yes (Refresh) |
| **Users** | `POST` | `/users` | Register a new user | No |
| | `GET` | `/users/me` | Get current user profile | Yes |
| **Posts** | `GET` | `/posts` | List all posts (with pagination/search/sort) | Yes |
| | `POST` | `/posts` | Create a new post | Yes |
| | `GET` | `/posts/{id}` | Get post details | Yes |
| | `DELETE` | `/posts/{id}` | Delete a post | Yes |
| | `PUT` | `/posts/{id}` | Update a post | Yes |
| **Comments**| `POST` | `/posts/{id}/comments` | Add a comment to a post | Yes |
| | `GET` | `/posts/{id}/comments` | List comments for a post | No |
| **Votes** | `POST` | `/vote` | Vote on a post | Yes |
| | `POST` | `/vote/toggle` | Toggle vote (Like/Unlike) | Yes |
| | `GET` | `/vote/{post_id}` | Get total votes for a post | No |
| **Health** | `GET` | `/health` | API & Database health check | No |

---

## ☁️ Deployment

This project is configured for one-click deployment on **Render** using a Blueprint.

### Deploy to Render
1. Push your code to GitHub.
2. In the Render Dashboard, click **New +** -> **Blueprint**.
3. Select this repository.
4. Render will use the `render.yaml` to provision a PostgreSQL database and a Web Service automatically.

---

## 🧪 Testing

Run the test suite using `pytest`:
```bash
pytest
```

**ER Diagram**

![fastapi - public](https://github.com/user-attachments/assets/fd5483ed-7abf-4943-a931-e8c9e365b17b)

---

