from app.models.schemas import users as _users_schemas


def get_user_db(username: str) -> _users_schemas.UserCreateResponse:
    return {
        "UserName": username,
        "UserID": "fake_user_id",
        "UserAge": 18,
    }
