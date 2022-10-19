from sqlalchemy.orm import Session, lazyload, joinedload
from models import Item

import models
import schemas


def get_items(db: Session):
    return db.query(models.Item).options(joinedload(Item.files)).all()


def get_files(db: Session):
    return db.query(models.Files).all()

def get_item(db: Session, id, password):
    return db.query(models.Item).options(joinedload(Item.files)).filter_by(id=id, password=password).first()


def add_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
