import logging
import os

from typing import Self

import aiosqlite

from src.utils.globals.get_app_path import get_app_path

class AsyncConnectionSqlite():

    def __init__(self: Self, file_database: str, autocommit: bool = True):
        """
        Inicializa a instância da conexão com o banco de dados.
        Carrega os métodos de configuração de acordo com a base informada.
        """
        self.path = get_app_path(2, f"{os.getenv("SQLITE_PATH")}/{file_database}")
        self.connection: aiosqlite.Connection | None = None
        self.autocommit = autocommit


    async def connect(self: Self) -> bool:
        try:
            self.connection = await aiosqlite.connect(self.path)
            self.connection.row_factory = aiosqlite.Row
            return True

        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error(
                "Falha ao acessar o banco de dados local: %s - %s",
                str(self.path),
                str(error),
            )

        return False


    async def close(self: Self):
        if self.connection:
            await self.connection.close()
