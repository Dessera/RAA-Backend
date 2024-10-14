from tortoise import fields, Model
from uuid import uuid1


class Role(Model):
    id = fields.UUIDField(pk=True, default=uuid1)
    name = fields.CharField(max_length=50, unique=True)
    description = fields.TextField(null=True)

    users = fields.ManyToManyField("models.User", related_name="roles")
    permissions = fields.ManyToManyField("models.Permission", related_name="roles")

    def __str__(self):
        return self.name

    class Meta:  # type: ignore
        table = "roles"


# class PermissionType(str, Enum):


class Permission(Model):
    id = fields.UUIDField(pk=True, default=uuid1)
    name = fields.CharField(max_length=50, unique=True)
    description = fields.TextField(null=True)

    roles = fields.ManyToManyField("models.Role", related_name="permissions")

    def __str__(self):
        return self.name

    class Meta:  # type: ignore
        table = "permissions"
