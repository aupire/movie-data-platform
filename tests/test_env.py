import pytest
from pydantic import ValidationError
from src.config.settings import Settings


def test_settings_loads_successfully():
    settings = Settings()
    assert settings.SMTP_HOST is not None
    assert settings.SMTP_PORT is not None
    assert settings.SMTP_USER is not None
    assert settings.SMTP_PASSWORD is not None


def test_invalid_db_port(monkeypatch):
    monkeypatch.setenv("SMTP_PORT", "not_an_int")

    with pytest.raises(ValidationError):
        Settings()


# test github action 3
