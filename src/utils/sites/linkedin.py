import asyncio
import logging

from pathlib import Path
from typing import Self

from playwright.async_api import Page

from src.utils.sites.site import Site

class Linkedin(Site):
    """Classe de consultar dados no site"""

    def __init__(self: Self, page: Page):
        super().__init__(page)

    def __del__(self: Self):
        super().__del__()


    async def insert_email(self: Self, email: str, wait_time: int = 0):
        try:
            email_locator = self.page.get_by_role(
                "textbox",
                name="E-mail ou telefone"
            )
            await email_locator.wait_for(state="visible")
            await email_locator.click(force=True)
            await email_locator.press("Control+A")
            await email_locator.type(email)
            await asyncio.sleep(wait_time)
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(e), str(e))


    async def insert_password(self: Self, password: str, wait_time: int = 0):
        try:
            password_locator = self.page.get_by_role(
                    "textbox",
                    name="Senha"
                )
            await password_locator.clear()
            await password_locator.focus()
            await password_locator.type(password)
            await asyncio.sleep(wait_time)
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(e), str(e))

    async def click_access(self: Self, wait_time: int = 0):
        try:
            await self.page.get_by_role("button", name="Entrar", exact=True).click()
            await asyncio.sleep(wait_time)
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(e), str(e))


    async def is_logged(self: Self, name: str) -> bool:
        try:
             return await self.page.get_by_text(
                name,
                exact=True
            ).is_visible()
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(e), str(e))

            
    async def send_image(self: Self, path: Path, wait_time: int = 0):
        try:
            async with self.page.expect_file_chooser() as fc_info:
                await self.page.get_by_role("link", name="Foto").click()
            file_chooser = await fc_info.value
            await file_chooser.set_files(path)
            await asyncio.sleep(wait_time)
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(e), str(e))


    async def click_advance(self: Self, wait_time: int = 0):
        try:
            dialog = self.page.get_by_role("dialog")
            next_button = dialog.locator("button.share-box-footer__primary-btn")
            await next_button.wait_for(state="visible")
            await next_button.click()
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))


    async def insert_publication_text(self: Self, link: str, wait_time: int = 0):
        try:
            await self.page.get_by_role("textbox", name="Editor de texto para criação") \
                .fill(f"🎵 Spotify:\n{link}")
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))



    async def click_schedule_post(self: Self, wait_time: int = 0):
        try:
            await self.page.get_by_role("button", name="Agendar publicação") \
                .click()
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))


    async def insert_date(self: Self, date: str, wait_time: int = 0):
        try:
            await self.page.get_by_role("textbox", name="Date").press("ControlOrMeta+a")
            await self.page.get_by_role("textbox", name="Date").fill(date)
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))


    async def insert_hour(self: Self, hour: str, wait_time: int = 0):
        try:
            await self.page.get_by_role("combobox", name="Time").press("ControlOrMeta+a")
            await self.page.get_by_role("combobox", name="Time").fill(hour)
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))


    async def click_schedule_advance(self: Self, wait_time: int = 0):
        try:
            await self.page.get_by_role("button", name="Avançar").click()
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))

    async def click_schedule(self: Self, wait_time: int = 0):
        try:
            await self.page.get_by_role("button", name="Agendar", exact=True).click()
            await asyncio.sleep(wait_time)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error("%s::%s",type(error), str(error))



#             <button aria-label="Avançar" id="ember140" class="share-box-footer__primary-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view" type="button"><!---->
# <span class="artdeco-button__text">
    
#               Avançar
          
# </span></button>