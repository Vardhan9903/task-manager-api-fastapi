# Task Manager API (FastAPI)

A simple Task Manager REST API built with Python and FastAPI.

## Features
- Create task
- Get all tasks
- Get task by ID
- Complete task
- Delete task

## 📁 Project Structure

task-manager-api-fastapi/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE

## API Endpoints

| Method | Endpoint        | Description          |
|--------|-----------------|----------------------|
| POST   | /tasks/         | Create a new task    |
| GET    | /tasks/         | Get all tasks        |
| GET    | /tasks/{id}     | Get task by ID       |
| PUT    | /tasks/{id}     | Update task by ID    |
| DELETE | /tasks/{id}     | Delete task by ID    |

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/Vardhan9903/task-manager-api-fastapi.git

2. Navigate into project:
   cd task-manager-api-fastapi

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   venv\Scripts\activate   (Windows)
   source venv/bin/activate (Mac/Linux)

5. Install dependencies:
   pip install -r requirements.txt

6. Run the server:
   uvicorn main:app --reload

