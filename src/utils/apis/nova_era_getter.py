import os

from requests.models import Response

from typing import Self, Dict, Any, Union

from src.core.api.collector_api import CollectorApi


class NovaEraGetter(CollectorApi):

    def __init__(self: Self) -> None:
        super().__init__()
        self.__url = os.environ["NOVA_ERA_URL_API"]
        self.__api_key = os.environ["NOVA_ERA_API_KEY_API"]

    def __del__(self: Self) -> None:
        super().__del__()
        self.__url = None
        self.__api_key = None

    def __set_header(self: Self, ) -> Dict[str, Any]:
        return {
            "Content-Type": "application/html",
            "Authorization": self.__api_key
        }

    def __set_body(self: Self, beneficio: Union[str, int]) -> Dict[str, Any]:
        return {
            "beneficio": beneficio
        }

    def get_all_data(self: Self, **kwargs: Dict[str, Any]) -> Response:
        benefict = kwargs.get("benefict")
        if benefict:
            url = self.__url
            header = self.__set_header()
            data = self.__set_body(benefict)

            self.set_url(url)
            self.set_header(header)
            self.set_body(data)

            return self.run_post()
