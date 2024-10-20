import pytest
from tortoise.contrib.test import finalizer, initializer
from openvault.models import SCHEMAS
from openvault.config import CONFIG


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    # db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory:")
    db_url = CONFIG.database_test_url
    initializer(SCHEMAS, db_url=db_url, app_label="models")
    request.addfinalizer(finalizer)
