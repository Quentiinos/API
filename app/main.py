from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()
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

# @router.get("/{prenom}")
# async def hello(prenom: str):
#     return {"response": f"Bonjour {prenom} !"}

@router.get("/users", response_model=list[schemas.UserWID])
async def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


app.include_router(router)
