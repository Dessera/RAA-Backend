from uuid import uuid1
from tortoise import fields
from tortoise.models import Model


class Group(Model):
    id = fields.UUIDField(primary_key=True, default=uuid1)
    name = fields.CharField(max_length=50, unique=True, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    disabled = fields.BooleanField(default=False)

    description = fields.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:  # type: ignore
        table = "groups"
