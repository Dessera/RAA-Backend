from openvault.schemas.user_schema import UserCreateSchema
from tortoise.contrib import test

from openvault.services import user_service


class TestUser(test.TestCase):
    async def test_get_user_list(self):
        res = await user_service.get_user_list()
        self.assertIsInstance(res, list)

    async def test_create_user(self):
        user = UserCreateSchema.model_validate(
            {
                "username": "test_user",
                "email": "test@user.com",
                "password": "test_password",
                "signature": "test_signature",
            }
        )
        res = await user_service.create_user(user)
        self.assertEqual(res.username, "test_user")
        self.assertIsNotNone(res.id)
