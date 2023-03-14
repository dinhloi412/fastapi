from pydantic import BaseModel, Field


class UserId(BaseModel):
    user_id: str = Field(..., alias="UserID")


class UserName(BaseModel):
    username: str = Field(..., alias="UserName")


class UserAge(BaseModel):
    age: int = Field(..., alias="UserAge")
