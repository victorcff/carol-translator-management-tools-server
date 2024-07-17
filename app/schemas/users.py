from pydantic import BaseModel
from time import time

class UserBase(BaseModel):
  username: str
  
class UserCreate(UserBase):
  password: str
  role: str
  
class UserResponse(UserBase):
  id: int
  created_at: time
  class Config:
    orm_mode = True
    from_attributes = True
  
class UserRequest(UserBase):
  ...