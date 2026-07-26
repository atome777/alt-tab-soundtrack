import os

from typing import Self, Dict, Any

from src.core.api.collector_api import CollectorApi


class ConsigilusGetter(CollectorApi):

    def __init__(self: Self) -> None:
        super().__init__()
        self.__url = os.environ["CONSIGILUS_URL_API"]
        self.__token = os.environ["CONSIGILUS_TOKEN_API"]

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
        cpf = kwargs.get("cpf")
        benefict = kwargs.get("benefict")
        url = f"{self.__url}/{endpoint}?cpf={cpf}&benefict={benefict}"
        header = self.__set_header()

        self.set_url(url)
        self.set_header(header)
        return self.run_get()

    def get_all_data(self: Self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Method:
            Coleta os contratos atraves do consigilus
        Args:
            cpf (str): cpf do abençoado
            benefict (str): matricula ou numero de beneficio

        Raises:
            ValueError: Caso data não seja informado

        Returns:
            Dict[str, Any]: resultado da busca
        """
        endpoint = "consig/contract"
        cpf = kwargs.get("cpf")
        benefict = kwargs.get("benefict")
        if not cpf or not benefict:
            raise ValueError(
                "Favor informar os dados a serem localizados no Credilus")

        return self.__query_get(endpoint=endpoint, cpf=cpf, benefict=benefict)
