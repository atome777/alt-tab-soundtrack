from io import BytesIO
from typing import Self, Dict, Any, Optional, Tuple

from aiohttp import ClientTimeout, ContentTypeError

import aiofiles

from src.configs.apis.async_connection_api import AsyncConnectionApi

class AsyncCollectorApi(AsyncConnectionApi):
        
    def __init__(self: Self):
        super().__init__()
        self._verify = False
        self._timeout = ClientTimeout(total=30)
        
        self._url: Optional[str] = None
        self._body: Optional[Dict[str, Any]] = None
        self._headers: Optional[Dict[str, Any]] = None
        self._proxy: Optional[str] = None

    async def set_timeout(self: Self, seconds: int = 30):
        self._timeout = ClientTimeout(total=seconds)

    async def set_url(self: Self, url: str):
        self._url = url

    async def set_body(self: Self, body: Dict[str, Any]):
        self._body = body

    async def set_header(self: Self, header: Dict[str, Any]):
        self._headers = header

    async def set_proxy(self: Self, proxy: str):
        self._proxy = proxy

    async def run_get(self: Self) -> Optional[Tuple[Any, int]]:
        """Executa um GET via requets"""
        if not self._url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self._headers:
            raise ValueError(
                "Favor informar os dados do header em formato dict")
        if self.session:
            async with self.session.get(
                url=self._url,
                timeout=self._timeout,
                headers=self._headers,
                proxy=self._proxy,
                ssl=False
            ) as response:
                try:
                    data = await response.json(content_type=None)
                    return data, response.status
                except (ContentTypeError, ValueError):
                    return {"text": response.text}, response.status
                finally:
                    await response.release()

    async def run_post(self: Self) -> Optional[Tuple[Any, int]]:
        """Executa um POST via requets"""
        if not self._url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self._body:
            raise ValueError("Favor informar os dados do body em formato dict")
        if self.session:
            async with self.session.post(
                url=self._url,
                timeout=self._timeout,
                headers=self._headers,
                json=self._body,
                proxy=self._proxy,
                ssl=False
            ) as response:
                try:
                    data = await response.json(content_type=None)
                    # data = await response.text()
                    return data, response.status
                except (ContentTypeError, ValueError):
                    return {"text": response.text}, response.status
                finally:
                    await response.release()

    async def run_put(self: Self) -> Optional[Tuple[Dict[str, Any], int]]:
        """Executa um PUT via requets"""
        if not self._url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self._body:
            raise ValueError("Favor informar os dados do body em formato dict")
        if self.session:
            async with self.session.put(
                url=self._url,
                timeout=self._timeout,
                headers=self._headers,
                json=self._body,
                proxy=self._proxy,
                ssl=False
            ) as response:
                try:
                    data = await response.json(content_type=None)
                    return data, response.status
                finally:
                    await response.release()

    async def run_patch(self: Self) -> Optional[Tuple[Dict[str, Any], int]]:
        """Executa um PATCH via requets"""
        if not self._url:
            raise ValueError("Favor informar a url a ser usada.")
        if not self._body:
            raise ValueError("Favor informar os dados do body em formato dict")
        if self.session:
            async with self.session.patch(
                url=self._url,
                timeout=self._timeout,
                headers=self._headers,
                json=self._body,
                proxy=self._proxy,
                ssl=False
            ) as response:
                try:
                    data = await response.json(content_type=None)
                    return data, response.status
                finally:
                    await response.release()

    async def run_delete(self: Self) -> Optional[Tuple[Dict[str, Any], int]]:
        """Executa um DELETE via requets"""
        if not self._url:
            raise ValueError("Favor informar a url a ser usada.")
        if self.session:
            async with self.session.delete(
                url=self._url,
                timeout=self._timeout,
                headers=self._headers,
                json=self._body,
                proxy=self._proxy,
                ssl=False
            ) as response:
                try:
                    data = await response.json(content_type=None)
                    return data, response.status
                finally:
                    await response.release()

    async def download_file(self: Self, url: str, filename: str):
        if self.session:
            async with self.session.get(
                url=url,
                timeout=self._timeout,
                headers=self._headers,
                proxy=self._proxy,
                ssl=False
                ) as response:
                response.raise_for_status()
                async with aiofiles.open(filename, "wb") as f:
                    async for chunk in response.content.iter_chunked(1024 * 64):
                        await f.write(chunk)

    async def download_file_bytes(self: Self, url: str) -> Optional[BytesIO]:
        buffer = BytesIO()
        if self.session:
            async with self.session.get(url) as response:
                response.raise_for_status()

                async for chunk in response.content.iter_chunked(1024 * 64):
                    buffer.write(chunk)

            buffer.seek(0)  # volta o ponteiro pro início
            return buffer