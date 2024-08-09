from fastapi import Depends, FastAPI, HTTPException, APIRouter, Response, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from app.config import Settings

app = FastAPI(
    title=Settings.APP_NAME
)
router = APIRouter(prefix="/api/v1")
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/hello")
async def hello_world():
    return {"message": "Hello World !"}

@router.get("/users", response_model=list[schemas.UserWID])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/users/id/{id}", response_model=schemas.UserWID)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return user

@router.get("/users/name/{name}", response_model=list[schemas.UserWID])
async def get_user_by_name(name: str, db: Session = Depends(get_db)):
    users = crud.get_user_by_name(db, name)
    if not users:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return users

@router.post("/users", response_model=schemas.UserWID, status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        return crud.create_user(db=db, user=user)

@router.delete("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="User not found")

    crud.delete_user(db, user)
    return {
        "detail": f"User: {user.name} {user.surname} (ID: {user.id}) deleted successfully !"
    }
 

app.include_router(router)
