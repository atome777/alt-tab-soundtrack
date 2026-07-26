import logging
import os

from src.utils.globals.get_app_path import get_app_path

def config_logger():
    """Configuração de logs da aplicação."""

    log_file = get_app_path(2, "/data/logs/app_logs.log")

    file_handler = logging.FileHandler(log_file, "a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    formatter_file_handler = logging.Formatter(
        "%(asctime)s::%(name)s::%(levelname)s::%(message)s")
    file_handler.setFormatter(formatter_file_handler)

    app_name = os.getenv("APP_NAME", "unknown")

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_format = f"%(asctime)s::{app_name}::%(message)s"
    formatter_stream_handle = logging.Formatter(stream_format)
    stream_handler.setFormatter(formatter_stream_handle)
    
    app_env = os.getenv("APP_ENV")

    if app_env == "production":
        logging.basicConfig(
            level=logging.INFO,
            handlers=[file_handler, stream_handler],
            force=True
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[file_handler, stream_handler],
            force=True
        )
