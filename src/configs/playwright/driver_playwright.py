from typing import Self
from playwright.async_api import Playwright, async_playwright


class DriverPlaywright:
    def __init__(self: Self):
        self._playwright: Playwright


    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

    async def start(self: Self):
        """Inicializa o Playwright."""
        self._playwright = await async_playwright().start()
    
    async def stop(self: Self):
        """Para o Playwright."""
        if self._playwright:
            await self._playwright.stop()
