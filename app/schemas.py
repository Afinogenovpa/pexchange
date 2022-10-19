from datetime import datetime
import typing
from pydantic import BaseModel
from typing import List, Optional


class Files(BaseModel):
    file_name: str

    class Config:
        orm_mode = True


class Item(BaseModel):
    id: int
    url: str
    files: list[Files]
    password: str
    body: str
    is_password_needed: bool
    to_delete: bool



    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    password: str
    body: Optional[str]
    is_password_needed: bool
    to_delete: bool
    time_to_delete: datetime


class ItemCreate(ItemBase):
    pass

    class Config:
        orm_mode = True

