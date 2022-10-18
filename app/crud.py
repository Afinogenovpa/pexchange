from sqlalchemy.orm import Session

import models
import schemas
import uuid


def get_items(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, uniq_id, password):
    return db.query(models.Item).filter_by(uniq_id=uniq_id, password=password).first()


def add_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.__dict__)
    # db_item.url = url
    # db_item.uniq_id = uniq_id
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
