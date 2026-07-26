from pathlib import Path

from src.utils.globals.get_app_path import get_app_path
from src.types.ui.html_data import HtmlData

TEMPLATE = get_app_path(2, "/templates/index.html")
OUTPUT = get_app_path(2, "/output/post.html")

async def html_generator(data: HtmlData) -> Path:

    html = TEMPLATE.read_text(encoding="utf-8")

    html = (
        html
        .replace("{{EDITION_NUMBER}}", data.get("edition_number"))
        .replace("{{SITUATION_TITLE}}", data.get("situation_title"))
        .replace("{{SITUATION}}", data.get("situation"))
        .replace("{{LINK_ALBUM}}", data.get("link_album"))
        .replace("{{MUSIC_TITLE}}", data.get("music_title"))
        .replace("{{MUSIC_ARTIST}}", data.get("muscic_artist"))
        .replace("{{CURIOSITY_TITLE}}", data.get("curiosity_title"))
        .replace("{{CURIOSITY}}", data.get("curiosity"))
        .replace("{{QUESTION_TITLE}}", data.get("question_title"))
        .replace("{{QUESTION}}", data.get("question"))
    )

    OUTPUT.write_text(html, encoding="utf-8")

    return OUTPUT
