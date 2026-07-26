import os

from typing import Self, Dict, Any

from src.core.api.collector_api import CollectorApi


class CredilusGetter(CollectorApi):

    def __init__(self: Self) -> None:
        super().__init__()
        self.__url = os.environ["CREDILUS_URL_API"]
        self.__token = os.environ["CREDILUS_TOKEN_API"]

    def __del__(self: Self) -> None:
        super().__del__()
        self.__url = None
        self.__token = None

    def __set_header(self: Self):
        return {
            "content-type": "application/json",
            "accept": "application/json",
            "Authorization": f"Bearer {self.__token}"
        }

    def __query_get(self: Self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        endpoint = kwargs.get("endpoint")
        data = kwargs.get("data")
        url = f"{self.__url}/consultas/{endpoint}/{data}"
        header = self.__set_header()

        self.set_url(url)
        self.set_header(header)
        return self.run_get()

    def get_all_data(self: Self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Method:
            Coleta dados via credilus
        Args:
            search_by (str): item de procura, ex.: umcpf, umnome, umnomecredilink
            data (str): item a ser procurado, ex.: "Nome do abençoado"

        Raises:
            ValueError: Caso data não seja informado

        Returns:
            Dict[str, Any]: resultado da busca
        """
        search_by = kwargs.get("search_by")
        data = kwargs.get("data")
        if not data:
            raise ValueError(
                "Favor informar os dados a serem localizados no Credilus")

        return self.__query_get(endpoint=search_by, data=data)
