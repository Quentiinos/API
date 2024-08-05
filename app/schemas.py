from pydantic import BaseModel

class UserBase(BaseModel):
    id: int

class UserWOID(BaseModel):
    surname: str
    name: str

class UserWID(UserBase):
    surname: str
    name: str

class UserCreate(UserBase):
    pass


class Config:
    orm_mode = True