from uuid import UUID
from fastapi import APIRouter
from ..services import user_service
from ..schemas.user_schema import (
    UserCreateSchema,
    UserLoginSchema,
    UserUpdateSchema,
    UserInfoSchema,
)

router = APIRouter(prefix="/users", tags=["User API"])


@router.post(
    path="/login",
    summary="用户登录",
    description="用户登录",
    response_model=UserInfoSchema,
)
async def login_user(user: UserLoginSchema):
    return await user_service.login_user(user)


@router.post(
    path="/",
    summary="创建用户",
    description="创建用户",
    response_model=UserInfoSchema,
)
async def create_user(user: UserCreateSchema):
    return await user_service.create_user(user)


@router.get(
    path="/",
    summary="获取用户列表",
    description="获取用户列表",
    response_model=list[UserInfoSchema],
)
async def get_user_list():
    return await user_service.get_user_list()


@router.get(
    path="/{user_id}",
    summary="获取用户信息",
    description="获取用户信息",
    response_model=UserInfoSchema,
)
async def get_user(user_id: UUID):
    return await user_service.get_user_by_id(user_id)


@router.put(
    path="/{user_id}",
    summary="更新用户信息",
    description="更新用户信息",
    response_model=UserInfoSchema,
)
async def update_user(user_id: UUID, user: UserUpdateSchema):
    return await user_service.update_user(user_id, user)


@router.delete(
    path="/{user_id}",
    summary="删除用户",
    description="删除用户",
)
async def delete_user(user_id: UUID):
    return await user_service.delete_user(user_id)
