from pydantic import BaseModel

class RegisterReq(BaseModel):
    name: str
    age: int = None
    email: str
    password: str