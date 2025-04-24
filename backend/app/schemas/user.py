from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    token: str
