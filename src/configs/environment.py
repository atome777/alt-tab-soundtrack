import logging
import os

from typing import Self
from pathlib import Path
from dotenv import load_dotenv

from src.configs.loggers.logger import config_logger


class Environment:

    def __init__(self: Self, dotenv_path: str | None = None) -> None:
        self.dotenv_path = Path(dotenv_path).resolve() if dotenv_path else self.__get_local_env_path()
        self.__load_all()

    def __get_local_env_path(self: Self):
        dotenv_path = Path(__file__).resolve().parents[1] / ".env"
        return Path(dotenv_path)

    def __load_local_env(self: Self):
        logging.debug("%s::Loading local env file", __name__)
        if self.dotenv_path.exists():
            load_dotenv(verbose=True, override=True, dotenv_path=self.dotenv_path)

        else:
            logging.error("%s::Local env file not found", __name__)

    def __load_system(self: Self):
        app_name = os.getenv("APP_NAME")
        if not app_name:
            raise ValueError("App name not set")

    def __show_dev_mode(self: Self):
        if os.getenv("APP_ENV") == "development":
            logging.warning("%s::APP IN DEV MODE",__name__)

    def __load_all(self: Self):
        logging.info("%s::Loading environment... Please wait", __name__)
        self.__load_local_env()
        self.__load_system()
        self.__show_dev_mode()
        config_logger()
        logging.info("%s::Environment is loaded...", __name__)
