from urllib import response
import pytest
from httpx import ASGITransport, AsyncClient
from openvault.models import init_db
from openvault.config import CONFIG
from openvault import app


@pytest.mark.asyncio
async def test_get_user_list():
    await init_db()
    async with AsyncClient(
        transport=ASGITransport(app), base_url=CONFIG.app_base_url
    ) as ac:
        response = await ac.get("/users/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
