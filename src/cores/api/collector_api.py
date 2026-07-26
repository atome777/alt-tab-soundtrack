import requests

from typing import Self, Dict, Any

from src.config.connection_api import ConnectionApi

from requests.exceptions import JSONDecodeError

from src.utils.exceptions.exceptions import ApiConsigError


class CollectorApi(ConnectionApi):

    def __init__(self: Self):
        super().__init__()
        self.__verify = False
        self.__timeout = 240

        self.__url = None
        self.__body = None
        self.__headers = None

    def __del__(self: Self):
        self.__url = None
        self.__body = None
        self.__headers = None

    def set_timeout(self: Self, seconds: int):
        self.__timeout = seconds

    def set_url(self: Self, url: str):
        self.__url = url

    def set_body(self: Self, body: Dict[str, Any]):
        self.__body = body

    def set_header(self: Self, header: Dict[str, Any]):
        self.__headers = header

    def _convert_json(self: Self, response: requests.Response):
        try:
            return response.json()
        except JSONDecodeError as json_decode_error:
            raise ApiConsigError(message=response) from json_decode_error

    def _raise_for_status(self: Self, response: requests.Response):
        """Raises :class:`HTTPError`, if one occurred."""
        if 400 <= response.status_code < 600:
            message_error = self._convert_json(response)
            if "message" in message_error:
                message = message_error["message"]
            else:
                message = response.text
            raise ApiConsigError(message=message)

    def run_get(self: Self) -> requests.Response:
        if not self.__url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self.__headers:
            raise ValueError(
                "Favor informar os dados do header em formato dict")
        response = requests.get(
            url=self.__url, verify=self.__verify, headers=self.__headers, timeout=self.__timeout)
        self._raise_for_status(response)
        return self._convert_json(response)

    def run_post(self: Self) -> requests.Response:
        if not self.__url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self.__body:
            raise ValueError("Favor informar os dados do body em formato dict")
        response = requests.post(
            url=self.__url, json=self.__body, verify=self.__verify, headers=self.__headers, timeout=self.__timeout)
        self._raise_for_status(response)
        return self._convert_json(response)

    def run_put(self: Self) -> requests.Response:
        if not self.__url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self.__body:
            raise ValueError("Favor informar os dados do body em formato dict")
        response = requests.put(
            url=self.__url, json=self.__body, verify=self.__verify, headers=self.__headers, timeout=self.__timeout)
        self._raise_for_status(response)
        return self._convert_json(response)

    def run_patch(self: Self) -> requests.Response:
        if not self.__url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self.__body:
            raise ValueError("Favor informar os dados do body em formato dict")
        response = requests.patch(
            url=self.__url, json=self.__body, verify=self.__verify, headers=self.__headers, timeout=self.__timeout)
        self._raise_for_status(response)
        return self._convert_json(response)

    def run_delete(self: Self) -> requests.Response:
        if not self.__url:
            raise ValueError("Favor informar a url a ser usada.")
        response = requests.delete(
            url=self.__url, verify=self.__verify, headers=self.__headers, timeout=self.__timeout)
        self._raise_for_status(response)
        return self._convert_json(response)
