from pathlib import Path
from typing import Self


from playwright.async_api import Page

from src.utils.sites.site import Site

class PostImage(Site):
    """Classe de consultar dados no site"""

    def __init__(self: Self, page: Page):
        super().__init__(page)

    def __del__(self: Self):
        super().__del__()

    async def get_screenshot(self: Self, path: Path):
        locator = self.page.locator("#app")
        await locator.screenshot(path=path)