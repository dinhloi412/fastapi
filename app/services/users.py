from pydantic import BaseModel
from app.models.schemas import users as _schemas_users
from app.utils import helpers as _helpers
from app.db.users import get_user_db
from app.db.entity import users as _users_entity

class UserService(BaseModel):
    def create_user(self, user_request: _schemas_users.UserCreateRequest) -> _schemas_users.UserCreateResponse:
        # Do something logical here
        _helpers.save_data(user_request)
        user_entity = _users_entity.UserEntity(**user_request.dict(by_alias=True)) 
        # Call db
        return user_entity

    def get_user(self, username: str) -> _schemas_users.UserCreateResponse:
        response = get_user_db(username)
        return response
