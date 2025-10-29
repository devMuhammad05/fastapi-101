from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import SQLModel, Field


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONICS = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONICS = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-hop'

class AlbumBase(SQLModel):
    title: str
    release_date: date


class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True) 


class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []


class BandCreate(BandBase):
    pass
    @field_validator('genre', mode='before')
    def title_case_genre(cls, value):
        return value.title() 

class BandWithID(BandBase):
    id: int