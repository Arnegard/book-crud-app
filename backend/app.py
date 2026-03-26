from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import Base, engine
from routes.book_routes import router as book_router

from models.book import Book

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5175"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router)


@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)