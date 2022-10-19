from datetime import datetime
from sqlalchemy import Boolean, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship



from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, unique=True, index=True, primary_key=True)
    url = Column(String, unique=True)
    password = Column(String)
    is_password_needed = Column(Boolean, default=False)
    body = Column(String)
    to_delete = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now())
    time_to_delete = Column(DateTime)

    files = relationship("Files", back_populates="owner", lazy="joined")


class Files(Base):
    __tablename__= "files"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String)

    owner_id = Column(Integer, ForeignKey("items.id"))
    owner = relationship("Item", back_populates="files")
