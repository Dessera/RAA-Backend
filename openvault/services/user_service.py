import bcrypt
import jwt
from uuid import UUID
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from tortoise.exceptions import DoesNotExist
from ..models.user_model import User
from ..config import CONFIG
from ..schemas.user_schema import (
    UserCreateSchema,
    UserUpdateSchema,
    UserInfoSchema,
    UserLoginSchema,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def create_access_token(user_id: UUID) -> str:
    time_expire = (
        datetime.now().timestamp()
        + timedelta(minutes=CONFIG.auth_token_expire_minutes).seconds
    )
    to_encode = {"sub": str(user_id), "exp": time_expire}
    return jwt.encode(
        to_encode, CONFIG.auth_secret_key, algorithm=CONFIG.auth_algorithm
    )


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, CONFIG.auth_secret_key, algorithms=[CONFIG.auth_algorithm])


async def login_user(user: UserLoginSchema) -> UserInfoSchema:
    crypted_password = hash_password(user.password)
    user_obj = await User.filter(
        **{user.login_type.value: user.login_value}, password=crypted_password
    ).first()
    if user_obj is None:
        raise DoesNotExist("User")
    return await UserInfoSchema.from_tortoise_orm(user_obj)


async def create_user(user: UserCreateSchema) -> UserInfoSchema:
    crypted_password = hash_password(user.password)
    user_obj = await User.create(
        **user.model_dump(exclude_unset=True, exclude={"password"}),
        password=crypted_password,
    )
    return await UserInfoSchema.from_tortoise_orm(user_obj)


async def get_user_by_id(user_id: UUID) -> UserInfoSchema:
    user_obj = await User.get(id=user_id)
    return await UserInfoSchema.from_tortoise_orm(user_obj)


async def get_user_by_username(username: str) -> UserInfoSchema:
    user_obj = await User.filter(username=username).first()
    if user_obj is None:
        raise DoesNotExist("User")
    return await UserInfoSchema.from_tortoise_orm(user_obj)


async def get_user_list() -> list[UserInfoSchema]:
    return await UserInfoSchema.from_queryset(User.all())


async def update_user(user_id: UUID, user: UserUpdateSchema) -> UserInfoSchema:
    await User.filter(id=user_id).update(**user.model_dump(exclude_unset=True))
    return await get_user_by_id(user_id)


async def delete_user(user_id: UUID) -> None:
    await User.filter(id=user_id).delete()
