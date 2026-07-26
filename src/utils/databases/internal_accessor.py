from typing import Self, Dict, Any

from src.core.database.collector_sqlite3 import CollectorSqlite3


class InternalGetter(CollectorSqlite3):

    def __init__(self: Self) -> None:
        super().__init__()

    def __del__(self: Self) -> None:
        super().__del__()

    def set_af(self: Self, **kwargs: Dict[str, Any]) -> int | Any:
        uuid = kwargs.get("user", {}).get("uuid")
        cpf = kwargs.get("user", {}).get("cpf")
        if kwargs.get("daemon", {}) is not None:
            af_codigo = kwargs.get("daemon", {}).get("codigo_af")
        else:
            af_codigo = None
        if uuid:
            upsert = "INSERT OR REPLACE INTO redux (uuid, cpf_representante, af_codigo) VALUES (?, ?, ?);"
            parameters = (uuid, cpf, af_codigo)

            return self.insert(upsert, parameters)

    def delete_af(self: Self, **kwargs: Dict[str, Any]):
        if kwargs.get("user") is not None:
            uuid = uuid = kwargs.get("user", {}).get("uuid")
            cpf = kwargs.get("user", {}).get("cpf")

            delete = "DELETE FROM redux where uuid = ? and cpf_representante = ?"
            parameters = (uuid, cpf)

            return self.delete(delete, parameters)

    def get_af(self: Self, **kwargs: Dict[str, Any]):
        if kwargs.get("user", {}) is not None:
            uuid = kwargs.get("user", {}).get("uuid")
            cpf = kwargs.get("user", {}).get("cpf")

            select = "SELECT * FROM redux where uuid = ? and cpf_representante = ?"
            parameters = (uuid, cpf)

            return self.get_one(select, parameters)
        
    def is_typping(self: Self, code_af: int):
        select = "SELECT * FROM redux WHERE af_codigo = ?"
        parameters = (code_af, )
        return self.get_one(select, parameters)
        
    def flush_af(self: Self):
        delete = "DELETE FROM redux"
        self.delete(delete)
