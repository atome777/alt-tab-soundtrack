import asyncio
import sys

from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[3]
sys.path.append(str(root))

from src.configs.environment import Environment
from src.services.database.internal import Internal

Environment()

async def test_insert():
    data_html = {'curiosity': '"Bitter Sweet Symphony" ficou marcada pelo final do filme Segundas Intenções e transmite exatamente essa sensação: algumas vitórias vêm acompanhadas de novos desafios.',
    'curiosity_title': 'Curiosidade',
    'edition_number': '003',
    'link_album': 'https://i.scdn.co/image/ab67616d0000aa54707d13d3f87652e737e94d45',
    'link_spotify': 'https://open.spotify.com/intl-pt/track/57iDDD9N9tTWe75x6qhStw',
    'music_artist': 'The Verve',
    'music_title': 'Bitter Sweet Symphony - Remastered 2016',
    'post_date': '27/07/2026',
    'post_hour': '03:33',
    'question': 'Qual música faz você pensar que finalmente deu tudo certo... até abrir o próximo e-mail?',
    'question_title': 'E para você?',
    'situation': 'Consegue resolver um problema ... e aparecem outros três.',
    'situation_title': 'Você está no trabalho e, de repente...'
    }
    id_post = await Internal().insert_post(**data_html)
    print("ID", id_post)


async def main():
    await test_insert()

if __name__ == "__main__":
    asyncio.run(main())