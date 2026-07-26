import os

from typing import Self, Dict, Any

from src.core.api.collector_api import CollectorApi


class BrxGetter(CollectorApi):

    def __init__(self: Self) -> None:
        super().__init__()
        self.__url_base = self.__mount_url_base()

    def __del__(self: Self) -> None:
        super().__del__()
        self.__url_base = None

    def __mount_url_base(self: Self) -> str:
        partial_url = os.environ["BRX_CONSIG_URL_API"].replace(
            "{TOKEN}", os.environ["BRX_CONSIG_TOKEN_API"])
        return partial_url

    def __mount_url(self: Self, cpf: str) -> str:
        return self.__url_base.replace("{CPF}", cpf.strip())

    def __set_header(self: Self) -> Dict[str, Any]:
        return {
            "content-type": "application/json"
        }

    def get_all_data(self: Self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        cpf = kwargs.get("cpf")
        if cpf:
            url = self.__mount_url(cpf)
            header = self.__set_header()
            self.set_header(header)
            self.set_url(url)
            return self.run_get()
