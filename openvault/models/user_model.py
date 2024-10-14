from tortoise import fields, Model
from uuid import uuid1


class User(Model):
    # Normal Keys
    id = fields.UUIDField(primary_key=True, default=uuid1)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=50, unique=True, null=True)
    password = fields.CharField(max_length=60)
    created_at = fields.DatetimeField(auto_now_add=True)
    disabled = fields.BooleanField(default=False)

    # Information Keys
    # not implemented yet (need minio)
    # avatar = fields.BinaryField(null=True)
    signature = fields.TextField(null=True)
    realname = fields.CharField(max_length=50, null=True)
    student_id = fields.CharField(max_length=8, null=True)

    # Foreign Keys
    # roles = fields.ManyToManyField("models.Role", related_name="users")

    def __str__(self):
        return self.username

    class Meta:  # type: ignore
        table = "users"
