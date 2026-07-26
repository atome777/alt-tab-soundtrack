from pathlib import Path

def get_app_path(parent: int, relative_path: str) -> Path:
    """Retorna um Path da aplicação"""
    base_path = str(Path(__file__).resolve().parents[parent])
    return Path("".join([base_path, relative_path]))