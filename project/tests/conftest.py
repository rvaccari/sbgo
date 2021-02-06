import pytest
from decouple import config
from starlette.testclient import TestClient

from app import main
from app.config import Settings, get_settings


def get_settings_override():
    return Settings(
        testin=True,
        database_url=config("DATABASE_TEST_URL", default="sqlite://sqlite.db"),
    )


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(main.app) as test_client:
        yield test_client
