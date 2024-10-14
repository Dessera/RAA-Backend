from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from pydantic import BaseModel
from enum import Enum
from typing import TYPE_CHECKING
from ..models.user_model import User


class UserLoginSchema(BaseModel):
    class LoginType(str, Enum):
        USERNAME = "username"
        EMAIL = "email"

    login_type: LoginType
    login_value: str
    password: str


if TYPE_CHECKING:

    class UserSchema(PydanticModel, User):  # type: ignore
        pass

    class UserCreateSchema(PydanticModel, User):  # type: ignore
        pass

    class UserUpdateSchema(PydanticModel, User):  # type: ignore
        pass

    class UserInfoSchema(PydanticModel, User):  # type: ignore
        pass
else:
    UserSchema = pydantic_model_creator(User, name="UserSchema")
    UserCreateSchema = pydantic_model_creator(
        User, name="UserCreateSchema", exclude_readonly=True
    )
    UserUpdateSchema = pydantic_model_creator(
        User,
        name="UserUpdateSchema",
        exclude_readonly=True,
        exclude=("password",),
        optional=(
            "username",
            "email",
            "disabled",
            "signature",
            "realname",
            "student_id",
        ),
    )
    UserInfoSchema = pydantic_model_creator(
        User,
        name="UserInfoSchema",
        exclude=("password",),
    )
