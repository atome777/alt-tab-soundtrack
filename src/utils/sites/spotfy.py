from typing import Self

from playwright.async_api import Page

from src.utils.sites.site import Site

class Spotfy(Site):
    """Classe de consultar dados no site"""

    def __init__(self: Self, page: Page):
        super().__init__(page)

    def __del__(self: Self):
        super().__del__()


    async def get_music_title(self: Self) -> str:
        return await self.page.locator('[data-testid="entityTitle"]').inner_text()

    async def get_music_artist(self: Self) -> str:
        return await self.page.locator('[data-testid="creator-link"]').inner_text()

    async def get_link_album(self: Self) -> str:
        image = self.page.locator('img[src*="i.scdn.co/image"]').first
        srcset = await image.get_attribute("srcset")

        if srcset:
            return srcset.split(",")[-1].strip().split(" ")[0]

        return image.get_attribute("src")
