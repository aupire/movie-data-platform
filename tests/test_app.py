import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_no_params(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {}


def test_single_param(client):
    response = client.get("/?foo=bar")
    assert response.status_code == 200
    assert response.get_json() == {"foo": "bar"}


def test_multiple_params(client):
    response = client.get("/?foo=bar&hello=world&number=42")
    assert response.status_code == 200
    assert response.get_json() == {"foo": "bar", "hello": "world", "number": "42"}
