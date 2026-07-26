"""Módulo que define a classe base Site para automação de páginas web."""

import os
import asyncio

from pathlib import Path
from typing import Self, Optional
from playwright.async_api import Page, Locator, Dialog


class Site:
    """Classe base para automação de páginas web com Playwright."""

    def __init__(self: Self, page: Page):
        self.page: Page = page
        self.time_out = int(os.getenv("PLAYWRIGHT_TIME_OUT", "60000"))
        self.alert_message: str | None = None

    def __del__(self: Self):
        del self.page
        del self.alert_message


    async def __get_dialog_text(self: Self, dialog: Dialog):
        """Armazena na variavel os dados da mensagem dialog"""
        self.alert_message = None
        self.alert_message = dialog.message
        await dialog.accept()


    async def handle_dialog_accept(self: Self):
        """Coleta o texto da mensagem e aceita"""
        self.page.on("dialog", self.__get_dialog_text)


    async def go_to_page(self: Self,
        url: str,
        force: bool = False,
        wait_time: int = 0,
        init_url: Optional[str] = None
    ):
        """Abre uma URL no browser"""
        if force:
            await self.page \
                .goto(url=url, wait_until="load", timeout=self.time_out, referer=init_url)
        else:
            if url not in self.page.url:
                await self.page \
                    .goto(url=url, wait_until="load", timeout=self.time_out, referer=init_url)

        await asyncio.sleep(wait_time)


    async def delete_image(self: Self,file_path: Path):
        """Deleta uma imagem salva"""
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)


    async def element_exist(self: Self, xpath: str) -> bool:
        """Verifica se o elemento esta visivel na pagina"""
        element: Locator = self.page \
            .locator(xpath)
        return await element.is_visible()

    async def set_tite_page(self: Self, title: str | None = None) -> None:
        """Define o título da página no browser"""
        if title:
            await self.page \
                .evaluate(f'document.title = "{title}";')
