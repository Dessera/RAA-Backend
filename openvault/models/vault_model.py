from enum import Enum
from uuid import uuid1
from tortoise import fields
from tortoise.models import Model


class VaultType(str, Enum):
    LOCAL = "local"
    GITHUB = "github"


class Vault(Model):
    id = fields.UUIDField(primary_key=True, default=uuid1)
    name = fields.CharField(max_length=50, unique=True, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    archived = fields.BooleanField(default=False)

    description = fields.TextField(null=True)
    vault_type = fields.CharEnumField(VaultType, default=VaultType.LOCAL)
    vault_link = fields.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:  # type: ignore
        table = "vaults"
