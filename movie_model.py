from pydantic import BaseModel
from typing import List

class MovieModel(BaseModel):

    title : str
    director : str
    keywords: List[str] = []
    year : int


