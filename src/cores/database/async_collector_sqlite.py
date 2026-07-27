from typing import Self, Any, Optional

from src.configs.databases.async_connection_sqlite import AsyncConnectionSqlite


class AsyncCollectorSqlite(AsyncConnectionSqlite):
    """
    Classe responsável por realizar operações de coleta e manipulação de dados
    em um banco SQLite de forma assíncrona.
    """

    def __init__(self: Self, file_database: str, autocommit: bool = True):
        super().__init__(file_database, autocommit)

    async def _commit_if_needed(self: Self) -> None:
        """
        Executa o commit caso o autocommit esteja habilitado.
        """
        if self.connection and self.autocommit:
            await self.connection.commit()

    async def get_one(
        self: Self,
        query: str,
        parameters: Optional[tuple[Any, ...]] = None
    ) -> Optional[dict[str, Any]]:
        """
        Executa um SELECT e retorna apenas uma linha.
        """
        if not self.connection:
            return None

        cursor = await self.connection.execute(query, parameters or ())
        row = await cursor.fetchone()
        await cursor.close()

        return dict(row) if row else None

    async def get_many(
        self: Self,
        query: str,
        parameters: Optional[tuple[Any, ...]] = None
    ) -> list[dict[str, Any]]:
        """
        Executa um SELECT e retorna todas as linhas encontradas.
        """
        if not self.connection:
            return []

        cursor = await self.connection.execute(query, parameters or ())
        rows = await cursor.fetchall()
        await cursor.close()

        return [dict(row) for row in rows]

    async def insert(
        self: Self,
        query: str,
        parameters: Optional[tuple[Any, ...]] = None
    ) -> Optional[int]:
        """
        Executa um INSERT no banco de dados.
        """
        if not self.connection:
            return None

        cursor = await self.connection.execute(query, parameters or ())
        last_id = cursor.lastrowid
        await cursor.close()

        await self._commit_if_needed()

        return last_id

    async def update(
        self: Self,
        query: str,
        parameters: Optional[tuple[Any, ...]] = None
    ) -> Optional[int]:
        """
        Executa um UPDATE no banco de dados.
        """
        if not self.connection:
            return None

        cursor = await self.connection.execute(query, parameters or ())
        affected = cursor.rowcount
        await cursor.close()

        await self._commit_if_needed()

        return affected

    async def delete(
        self: Self,
        query: str,
        parameters: Optional[tuple[Any, ...]] = None
    ) -> Optional[int]:
        """
        Executa um DELETE no banco de dados.
        """
        if not self.connection:
            return None

        cursor = await self.connection.execute(query, parameters or ())
        affected = cursor.rowcount
        await cursor.close()

        await self._commit_if_needed()

        return affected

    async def execute_many(
        self: Self,
        query: str,
        parameters: list[tuple[Any, ...]]
    ) -> None:
        """
        Executa um executemany no banco de dados.
        """
        if not self.connection:
            return

        await self.connection.executemany(query, parameters)
        await self._commit_if_needed()

    async def begin(self: Self) -> None:
        """
        Inicia uma transação manual.
        """
        if self.connection:
            await self.connection.execute("BEGIN")

    async def commit(self: Self) -> None:
        """
        Confirma a transação atual.
        """
        if self.connection:
            await self.connection.commit()

    async def rollback(self: Self) -> None:
        """
        Desfaz a transação atual.
        """
        if self.connection:
            await self.connection.rollback()

    async def disconnect(self: Self) -> None:
        """
        Fecha a conexão com o banco.
        """
        await self.close()