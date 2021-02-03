import logging
from functools import lru_cache

from decouple import config
from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = config("ENVIRONMENT", "dev")
    testing: bool = config("TESTING", default=False, cast=bool)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
