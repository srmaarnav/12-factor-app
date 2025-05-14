from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_base_url: str
    api_key: str
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
