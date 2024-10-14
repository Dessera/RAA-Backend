import bcrypt
import jwt
from uuid import UUID
from ..models.group_model import Group
from ..schemas.group_schema import (
    GroupCreateSchema,
    GroupUpdateSchema,
    GroupInfoSchema,
)


async def create_group(group: GroupCreateSchema) -> GroupInfoSchema:
    group_obj = await Group.create(**group.model_dump(exclude_unset=True))
    return await GroupInfoSchema.from_tortoise_orm(group_obj)


async def get_group_list() -> list[GroupInfoSchema]:
    return await GroupInfoSchema.from_queryset(Group.all())


async def get_group_by_id(group_id: UUID) -> GroupInfoSchema:
    group_obj = await Group.get(id=group_id)
    return await GroupInfoSchema.from_tortoise_orm(group_obj)


async def update_group(group_id: UUID, group: GroupUpdateSchema) -> GroupInfoSchema:
    await Group.filter(id=group_id).update(**group.model_dump(exclude_unset=True))
    return await get_group_by_id(group_id)


async def remove_group(group_id: UUID):
    await Group.filter(id=group_id).delete()
