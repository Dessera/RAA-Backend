from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from pydantic import BaseModel
from enum import Enum
from typing import TYPE_CHECKING
from ..models.vault_model import Vault

if TYPE_CHECKING:

    class VaultSchema(PydanticModel, Vault):  # type: ignore
        pass

    class VaultCreateSchema(PydanticModel, Vault):  # type: ignore
        pass

    class VaultUpdateSchema(PydanticModel, Vault):  # type: ignore
        pass

    class VaultInfoSchema(PydanticModel, Vault):  # type: ignore
        pass
else:
    VaultSchema = pydantic_model_creator(Vault, name="VaultSchema")
    VaultCreateSchema = pydantic_model_creator(
        Vault, name="VaultCreateSchema", exclude_readonly=True
    )
    VaultUpdateSchema = pydantic_model_creator(
        Vault,
        name="VaultUpdateSchema",
        exclude_readonly=True,
        exclude=("vault_type", "vault_link"),
        optional=("name", "description", "archived"),
    )
    VaultInfoSchema = pydantic_model_creator(
        Vault,
        name="VaultInfoSchema",
    )
