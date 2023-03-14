from app.models.domains import users as _users_domains


class UserCreateRequest(
    _users_domains.UserId, _users_domains.UserName,
    _users_domains.UserAge
):
    pass


class UserCreateResponse(UserCreateRequest):
    pass
