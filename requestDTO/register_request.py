from pydantic import BaseModel, Field

class RegisterReq(BaseModel):
    name: str
    age: int = None
    email: str
    password: str