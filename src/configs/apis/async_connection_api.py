from typing import Self, Optional

from aiohttp import ClientSession

class AsyncConnectionApi():

    def __init__(self: Self):
        self.session: Optional[ClientSession] = None

    async def connect(self: Self):
        if not self.session or self.session.closed:
            self.session = ClientSession()

    async def disconnect(self: Self):
        if self.session and not self.session.closed:
            await self.session.close()
