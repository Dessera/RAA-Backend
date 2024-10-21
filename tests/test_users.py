from openvault.schemas.user_schema import UserCreateSchema
from tortoise.contrib import test

from openvault.services import user_service


class TestUser(test.TestCase):
    TEST_USER = UserCreateSchema.model_validate(
        {
            "username": "test_user",
            "email": "test@user.com",
            "password": "test_password",
            "signature": "test_signature",
        }
    )

    def test_hash_password(self):
        password = "test_password"
        hashed_password = user_service.hash_password(password)
        self.assertTrue(user_service.verify_password(password, hashed_password))

    async def test_get_user_list(self):
        res = await user_service.get_user_list()
        self.assertIsInstance(res, list)

    async def test_create_user(self):
        res = await user_service.create_user(TestUser.TEST_USER)
        self.assertEqual(res.username, "test_user")
        self.assertIsNotNone(res.id)

    async def test_get_user_by_id(self):
        user = await user_service.create_user(TestUser.TEST_USER)
        res = await user_service.get_user_by_id(user.id)
        self.assertEqual(res.username, "test_user")
