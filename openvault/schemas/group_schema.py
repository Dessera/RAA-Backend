from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from typing import TYPE_CHECKING
from ..models.group_model import Group

if TYPE_CHECKING:

    class GroupSchema(PydanticModel, Group):  # type: ignore
        pass

    class GroupCreateSchema(PydanticModel, Group):  # type: ignore
        pass

    class GroupUpdateSchema(PydanticModel, Group):  # type: ignore
        pass

    class GroupInfoSchema(PydanticModel, Group):  # type: ignore
        pass

else:
    GroupSchema = pydantic_model_creator(Group, name="GroupSchema")
    GroupCreateSchema = pydantic_model_creator(
        Group, name="GroupCreateSchema", exclude_readonly=True
    )
    GroupUpdateSchema = pydantic_model_creator(
        Group,
        name="GroupUpdateSchema",
        exclude_readonly=True,
        optional=("name", "description", "disabled"),
    )
    GroupInfoSchema = pydantic_model_creator(
        Group,
        name="GroupInfoSchema",
    )
