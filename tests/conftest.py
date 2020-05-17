import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def cli():
    return TestClient(app)
