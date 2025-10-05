from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    WEB_SOCKET_URL: str
    WEB_SOCKET_HOST: str
    WEB_SOCKET_PORT: int

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()