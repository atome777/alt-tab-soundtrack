import logging
from typing import Self, Unpack

from src.cores.database.async_collector_sqlite import AsyncCollectorSqlite
from src.types.ui.html_data import HtmlData


class InternalAccessor(AsyncCollectorSqlite):

    def __init__(self: Self) -> None:
        self.file_database = "internal.db"
        super().__init__(self.file_database, True)


    async def insert_post(self: Self, **kwargs: Unpack[HtmlData]):
        try:
            await self.connect()
            if self.connection:

                link_spotify = kwargs.get("link_spotify")
                edition_number = kwargs.get("edition_number")
                music_title = kwargs.get("music_title")
                music_artist = kwargs.get("music_artist")
                link_album = kwargs.get("link_album")
                situation_title = kwargs.get("situation_title")
                situation = kwargs.get("situation")
                curiosity_title = kwargs.get("curiosity_title")
                curiosity = kwargs.get("curiosity")
                question_title = kwargs.get("question_title")
                question = kwargs.get("question")
                post_date = kwargs.get("post_date")
                post_hour = kwargs.get("post_hour")

                insert = """
                    INSERT INTO posts
                    (
                        link_spotify,
                        edition_number,
                        music_title,
                        music_artist,
                        link_album,
                        situation_title,
                        situation,
                        curiosity_title,
                        curiosity,
                        question_title,
                        question,
                        post_date,
                        post_hour
                    )
                    VALUES
                    (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )
                """
                parameters = (
                    link_spotify,
                    edition_number,
                    music_title,
                    music_artist,
                    link_album,
                    situation_title,
                    situation,
                    curiosity_title,
                    curiosity,
                    question_title,
                    question,
                    post_date,
                    post_hour,
                )

                return await self.insert(insert, parameters)
        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error(
                "InternalAccessor.insert_post error::%s", str(error)
            )
        finally:
            await self.close()


    async def get_last_post(self: Self, ):
        try:
            await self.connect()
            if self.connection:
                select = """
                    SELECT
                        *
                    FROM posts
                    ORDER BY
                        edition_number DESC
                    LIMIT
                        1;
                """
                return await self.get_one(select)

        except Exception as error: # pylint: disable=broad-exception-caught
            logging.error(
                "InternalAccessor.get_last_post error::%s", str(error)
            )
        finally:
            await self.close()
