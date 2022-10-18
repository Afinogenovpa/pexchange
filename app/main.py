from ast import For
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from re import I
from fastapi import Depends, FastAPI, HTTPException, Form, File, Form, UploadFile, Body
from sqlalchemy.orm import Session
import uvicorn
import models
import crud
import schemas
from datetime import datetime, timedelta
from database import SessionLocal, engine
from typing import Optional, Union
import uuid

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/data/", response_model=list[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items


@app.post("/data/")
def add_new_item(
        db: Session = Depends(get_db),
        password: Optional[str] = Form(default=""),
        body: Optional[str] = Form(),
        is_password_needed: Optional[bool] = Form(default=False),
        to_delete: Optional[bool] = Form(default=True),
        time_to_delete: Optional[datetime] = Body(default=datetime.now() + timedelta(days=3))):

    item = schemas.Item(
        uniq_id=uuid.uuid4().hex[:10].upper(),
        url=uuid.uuid4().hex[:10].upper(),
        file_name="file",
        password=password,
        body=body,
        is_password_needed=is_password_needed,
        to_delete=to_delete,
        created=datetime.now(),
        time_to_delete=datetime.now() + timedelta(days=3)
    )

    return crud.add_item(db=db, item=item)


@app.get("/data/{uniq_id}:{password}")
def get_item(uniq_id: str, password: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, uniq_id=uniq_id, password=password)
    return item


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
