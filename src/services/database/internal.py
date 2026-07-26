from typing import Self

from src.utils.database.internal_getter import InternalGetter


class Internal(InternalGetter):

    def __init__(self: Self) -> None:
        super().__init__()

    def __del__(self: Self) -> None:
        super().__del__()
