import asyncio
import sys
import threading

from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from src.ui.home import App

from src.configs.environment import Environment

loop = asyncio.new_event_loop()

if len(sys.argv) > 1:
    dotenv_path = sys.argv[1]
    Environment(dotenv_path=dotenv_path)
else:
    Environment()

def start_loop():
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":

    threading.Thread(
        target=start_loop,
        daemon=True
    ).start()

    app = App(loop)
    app.mainloop()

    loop.call_soon_threadsafe(loop.stop)
