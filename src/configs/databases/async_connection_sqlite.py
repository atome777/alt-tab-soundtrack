import logging
import os

from typing import Self

import aiosqlite

from src.utils.globals.get_app_path import get_app_path

class AsyncConnectionSqlite():

    def __init__(self: Self, path: str):
        """
        Inicializa a instância da conexão com o banco de dados.
        Carrega os métodos de configuração de acordo com a base informada.
        """
        self.path = get_app_path(2, f"{os.getenv("SQLITE_PATH")}/{path}")
        self.db: aiosqlite.Connection | None = None


    async def connect(self: Self):
        try:
            self.db = await aiosqlite.connect(self.path)
            self.db.row_factory = aiosqlite.Row


    async def close(self: Self):
        if self.db:
            await self.db.close()
