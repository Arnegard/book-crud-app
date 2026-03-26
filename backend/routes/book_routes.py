from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models.book import Book
from schemas.book_schema import BookCreate, BookUpdate, BookResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        year=book.year
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/books", response_model=list[BookResponse], status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.get("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.put("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, updated_book: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    book.title = updated_book.title
    book.author = updated_book.author
    book.genre = updated_book.genre
    book.year = updated_book.year

    db.commit()
    db.refresh(book)
    return book


@router.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}