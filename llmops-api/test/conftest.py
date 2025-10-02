import pytest

from app.http.app import app

@pytest.fixture
def clinet():
    app.config["TESTING"] = True
    with app.test_client() as clinet:
        yield clinet