# Book CRUD App
# Michael Holst

Fullstack CRUD-app with FastAPI (backend) and React (frontend).

## Start backend

cd backend
py -m pip install -r requirements.txt
py app.py

## Start frontend

cd frontend
npm install
npm run dev

## URLs

Frontend:
http://localhost:5175

Backend:
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs

## Endpoints

- POST /books
- GET /books
- GET /books/{id}
- PUT /books/{id}
- DELETE /books/{id}

## Tech stack

- FastAPI
- React
- SQLite
- SQLAlchemy
- Pydantic
