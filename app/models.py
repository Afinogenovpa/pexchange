import base64
from email.policy import default
from enum import unique
from random import random
from re import T
from venv import create
from datetime import datetime, timedelta
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, true, DateTime
import uuid



from database import Base


class Item(Base):
    __tablename__ = "items"

    uniq_id = Column(String, unique=True, index=True, primary_key=True)
    url = Column(String, unique=True)
    file_name = Column(String)
    password = Column(String)
    is_password_needed = Column(Boolean, default=False)
    body = Column(String)
    
    to_delete = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now())
    time_to_delete = Column(DateTime)

    


