import logging
from functools import lru_cache
from pathlib import PurePath
from typing import Dict

from decouple import AutoConfig
from pydantic import BaseSettings
from pydantic.networks import AnyUrl

APP_ROOT_FOLDER = PurePath(__file__).parent.parent

log = logging.getLogger(__name__)
config = AutoConfig(search_path=APP_ROOT_FOLDER)

APP_MODELS = [
    "app.models",
]


class Settings(BaseSettings):
    minutes_cache_offer = config("MINUTES_CACHE_OFFER", default=10, cast=int)
    environment: str = config("ENVIRONMENT", default="dev")
    testing: bool = config("TESTING", default=False, cast=bool)
    database_url: AnyUrl = config("DATABASE_URL", default="sqlite://sqlite.db")
    database_url_test: AnyUrl = config(
        "DATABASE_URL_TEST", default="sqlite://sqlite.db"
    )
    partner_host: str = config("PARTNER_HOST", default="127.0.0.1")
    partner_timeout: int = config("PARTNER_TIMEOUT", default=30)
    modules: Dict[str, list] = {"models": APP_MODELS}


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
