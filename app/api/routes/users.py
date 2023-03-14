from fastapi import APIRouter, Body, Depends, HTTPException
from app.models.schemas import users as _users_schemas
from app.services.users import UserService
router = APIRouter(
    prefix="/users"
)

user_service = UserService()


@router.post(
    "", response_model=_users_schemas.UserCreateResponse,
)
async def create_user(
    user: _users_schemas.UserCreateRequest
) -> _users_schemas.UserCreateResponse:
    # Authorization here
    return user_service.create_user(user)


@router.get(
    "", response_model=_users_schemas.UserCreateResponse,
)
async def get_user(
    username: str,
) -> _users_schemas.UserCreateResponse:
    # Authorization here
    return user_service.get_user(username)
