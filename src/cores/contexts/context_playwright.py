import os
from typing import Self, Optional

from playwright.async_api import Browser

from src.configs.playwright.driver_playwright import DriverPlaywright
from src.utils.globals.str_to_bool import str_to_bool
from src.types.proxies.proxy_playwright import ProxyPlaywright

class ContextPlaywright(DriverPlaywright):

    def __init__(self: Self, proxy: Optional[ProxyPlaywright]):
        super().__init__()
        self.proxy: Optional[ProxyPlaywright] = proxy
        self.playwright_headless: bool = str_to_bool(os.getenv("PLAYWRIGHT_HEADLESS", "False"))


    async def init_browser_chrome(self: Self) -> Browser:
        """Inicia o browser chromium."""
        return await self._playwright.chromium.launch(
            proxy=self.proxy, # type: ignore
            headless=self.playwright_headless,
            args=["--js-flags=--disable-break"]
        )
    
    async def init_browser_msedge(self: Self) -> Browser:
        """Inicia o browser msedge."""
        return await self._playwright.chromium.launch(
            proxy=self.proxy, # type: ignore
            channel= 'msedge',
            headless=self.playwright_headless,
            args=[
                "--start-maximized",
            ],
        )
    
    async def init_browser_firefox(self: Self) -> Browser:
        """Inicia o browser firefox."""
        return await self._playwright.firefox.launch(
            proxy=self.proxy, # type: ignore
            headless=self.playwright_headless,
            args=["--start-maximized"],
        )