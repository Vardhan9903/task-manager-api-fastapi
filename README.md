# Task Manager API (FastAPI)

A scalable Task Manager REST API built using FastAPI and Python.  
This project demonstrates real-world backend development with persistent database integration and clean API design.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) tasks
- FastAPI with automatic Swagger UI
- Persistent data storage using SQLite
- SQLAlchemy ORM for database models
- Clean and modular backend structure
- Beginner-friendly & production-style layout

---

## 🛠 Tech Stack

- Python 3.9+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic v2

---

## 📁 Project Structure

task-manager-api-fastapi/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── tasks.db
├── README.md
└── LICENSE

---

## 🔗 API Endpoints

| Method | Endpoint        | Description          |
|--------|-----------------|----------------------|
| POST   | /tasks/         | Create a new task    |
| GET    | /tasks/         | Get all tasks        |
| GET    | /tasks/{id}     | Get task by ID       |
| PUT    | /tasks/{id}     | Update task by ID    |
| DELETE | /tasks/{id}     | Delete task by ID    |

---

## ⚙️ How to Run Locally

1. Clone the repository:
git clone https://github.com/Vardhan9903/task-manager-api-fastapi.git

2. Navigate into project:
cd task-manager-api-fastapi

3. Create virtual environment:
python -m venv venv

4. Activate virtual environment:
Windows:
venv\Scripts\activate

5. Install dependencies:
pip install -r requirements.txt

6. Run the server:
python -m uvicorn main:app --reload

7. Open Swagger UI:
http://127.0.0.1:8000/docs

---

## 🗄 Database Integration

This project uses SQLite with SQLAlchemy ORM for persistent data storage.

Features:
- SQLite database (tasks.db)
- SQLAlchemy ORM models
- Persistent CRUD operations
- Database inspection using DB Browser for SQLite
- Compatible with Pydantic v2

## 📊 Accessing the Database

To view and run SQL queries on the database:

1. Install DB Browser for SQLite
2. Open tasks.db
3. Use Browse Data and Execute SQL tabs

Example SQL:
SELECT * FROM tasks;

---

## 👤 Author

Vardhan

---

## 📝 License

This project is licensed under the MIT License.
