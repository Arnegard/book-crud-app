from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    genre: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=0, le=2100)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True