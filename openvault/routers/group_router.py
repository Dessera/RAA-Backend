from uuid import UUID
from fastapi import APIRouter
from ..services import group_service
from ..schemas.group_schema import (
    GroupCreateSchema,
    GroupUpdateSchema,
    GroupInfoSchema,
)

router = APIRouter(prefix="/groups", tags=["Group API"])


@router.post(
    path="/",
    summary="创建组织",
    description="创建组织",
    response_model=GroupInfoSchema,
)
async def create_group(group: GroupCreateSchema):
    return await group_service.create_group(group)


@router.get(
    path="/",
    summary="获取组织列表",
    description="获取组织列表",
    response_model=list[GroupInfoSchema],
)
async def get_group_list():
    return await group_service.get_group_list()


@router.get(
    path="/{group_id}",
    summary="获取组织信息",
    description="获取组织信息",
    response_model=GroupInfoSchema,
)
async def get_group(group_id: UUID):
    return await group_service.get_group_by_id(group_id)


@router.put(
    path="/{group_id}",
    summary="更新组织信息",
    description="更新组织信息",
    response_model=GroupInfoSchema,
)
async def update_group(group_id: UUID, group: GroupUpdateSchema):
    return await group_service.update_group(group_id, group)


@router.delete(
    path="/{group_id}",
    summary="删除组织",
    description="删除组织",
)
async def remove_group(group_id: UUID):
    return await group_service.remove_group(group_id)
