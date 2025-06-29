from pydantic import BaseModel


class Book(BaseModel):
    id:int
    title:str
    author:str
    reviewer:str
    rating:float
    review:str
    date:str