from typing import Self

from src.utils.databases.internal_accessor import InternalAccessor

class Internal(InternalAccessor):

    def __init__(self: Self) -> None:
        super().__init__()
