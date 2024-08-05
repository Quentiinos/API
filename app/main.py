from fastapi import Depends, FastAPI, HTTPException, APIRouter
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

@router.get("/users/id/{id}", response_model=list[schemas.UserWID])
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, id)

@router.get("/users/name/{name}", response_model=list[schemas.UserWID])
async def get_user_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_user_by_name(db, name)


app.include_router(router)
