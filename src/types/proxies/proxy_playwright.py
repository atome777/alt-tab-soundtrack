from typing import TypedDict, Optional

class ProxyPlaywright(TypedDict):
    server: str
    username: Optional[str]
    password: Optional[str]
