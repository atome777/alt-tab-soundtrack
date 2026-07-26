from pathlib import Path
from typing import Self, List, Optional

from playwright.async_api import BrowserContext, Page

from src.cores.contexts.context_playwright import ContextPlaywright
from src.utils.browsers.engines import Engines
from src.types.proxies.proxy_playwright import ProxyPlaywright


class BrowserPlaywright(ContextPlaywright):

    def __init__(self: Self, proxy: Optional[ProxyPlaywright] = None):
        super().__init__(proxy)
        self._context: BrowserContext

    async def create_context(
        self: Self,
        engine: Engines,
        path_storage: Optional[Path] = None
    ) -> BrowserContext:
        """Cria um novo contexto de browser"""

        await self.start()

        if engine.value == "firefox":
            browser = await self.init_browser_firefox()
        elif engine.value == "chrome":
            browser = await self.init_browser_chrome()
        else:
            browser = await self.init_browser_msedge()

        kwargs = {
            "no_viewport": True,
        }

        # Carrega a sessão somente se o arquivo existir
        if path_storage and path_storage.exists():
            kwargs["storage_state"] = str(path_storage)

        self._context = await browser.new_context(**kwargs)

        return self._context

    async def save_storage(self, path: Path):
        """Salva cookies e sessão atual."""
        path.parent.mkdir(parents=True, exist_ok=True)
        await self._context.storage_state(path=str(path))

    async def create_list_pages(
        self: Self,
        engine: Engines,
        quantity: int = 1
    ) -> List[Page]:
        self._context = await self.create_context(engine)

        tabs = []

        for _ in range(quantity):
            tabs.append(await self._context.new_page())

        return tabs

    async def create_page(
        self: Self,
        engine: Engines,
        path_storage: Optional[Path] = None
    ) -> Page:
        self._context = await self.create_context(engine, path_storage)
        return await self._context.new_page()

    async def get_cookie(self):
        return await self._context.cookies()

    async def set_api_request_context(self):
        return self._context.request

    async def close_context(self: Self):
        if self._context:
            await self._context.close()

        await self.stop()