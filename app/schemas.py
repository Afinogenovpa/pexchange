from datetime import datetime
from fastapi import Form
import imp
from sqlite3 import Timestamp
from fastapi import Form
from pydantic import BaseModel
from typing import Optional
import uuid


class Item(BaseModel):
    uniq_id: str
    url: str
    file_name: str
    password: str
    body: str
    is_password_needed: bool
    to_delete: bool
    created: datetime
    time_to_delete: datetime


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
