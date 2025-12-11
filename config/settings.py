from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASSWORD: str
    model_config = SettingsConfigDict()


settings = Settings()
