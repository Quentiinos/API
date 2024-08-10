from sqlalchemy.orm import Session
from . import models, schemas

def get_users(db: Session):
    return db.query(models.User).order_by(models.User.id.asc()).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).order_by(models.User.id.asc()).all()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(surname=user.surname, name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user: models.User, updated_user: schemas.UserCreate):
    user.name = updated_user.name
    user.surname = updated_user.surname
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
