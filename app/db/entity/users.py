from app.models.schemas import users as _users_schemas


class UserEntity(_users_schemas.UserCreateRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_id(self, user_id: str) -> str:
        return user_id
