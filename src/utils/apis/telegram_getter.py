import os
import time

from typing import Self, Dict, Any
from requests import exceptions

from src.core.api.collector_api import CollectorApi


class TelegramGetter(CollectorApi):

    def __init__(self: Self) -> None:
        super().__init__()
        self.__url = os.environ["TELEGRAM_URL"]
        self.__token = os.environ["TELEGRAM_TOKEN"]
        self.__id = os.environ["TELEGRAM_CHAT_ID"]

    def __del__(self: Self) -> None:
        super().__del__()
        self.__url = None
        self.__token = None
        self.__id = None

    def send_message(self: Self, **kwargs: Dict[str, Any]):
        message = kwargs.get("message")
        if not message:
            raise ValueError(
                "Favor informar o texto para ser enviado via telegram")
        try:
            url = self.__url.replace("{TOKEN}", self.__token)
            data = {
                "chat_id": self.__id,
                "parse_mode": "HTML",
                "text": message
            }
            self.set_url(url)
            self.set_body(data)
            self.run_post()

        except (exceptions.HTTPError, exceptions.ConnectionError)as requests_exceptions:
            print("Aguardando, 30 para reenvio:",
                  requests_exceptions)
            time.sleep(30)
            self.send_message(message=message)

            time.sleep(1)
