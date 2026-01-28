from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr


class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: Optional[datetime] = None


class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int


class ErrorResponse(BaseModel):
    error: str
    message: str
