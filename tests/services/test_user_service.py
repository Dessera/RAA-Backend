import pytest
from openvault.models import init_db
from openvault.services import user_service
from openvault.schemas.user_schema import UserCreateSchema


@pytest.mark.asyncio
async def test_create_user():
    test_user = UserCreateSchema.model_validate(
        {
            "username": "test",
            "password": "test",
            "email": "test@test.com",
            "signature": "test signature",
            "realname": "test",
            "student_id": "12345678",
        }
    )
    user = await user_service.create_user(test_user)
    assert user.username == "test"


@pytest.mark.asyncio
async def test_get_user_by_username():
    user = await user_service.get_user_by_username("test")
    assert user.username == "test"
