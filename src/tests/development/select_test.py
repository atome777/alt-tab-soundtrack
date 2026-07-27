import asyncio
import sys

from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[3]
sys.path.append(str(root))

from src.configs.environment import Environment
from src.services.database.internal import Internal

Environment()

async def test_select():

    last_post = await Internal().get_last_post()
    print("Last Post", last_post)


async def main():
    await test_select()

if __name__ == "__main__":
    asyncio.run(main())