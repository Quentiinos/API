from sqlalchemy.orm import Session

from . import models, schemas

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(surname=user.surname, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()