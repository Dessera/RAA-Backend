import pytest
from tortoise.contrib.test import finalizer, initializer

from openvault.config import CONFIG
from openvault.models import SCHEMAS


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    print(SCHEMAS)
    initializer(SCHEMAS, db_url=CONFIG.database_url, app_label="models")
    request.addfinalizer(finalizer)
