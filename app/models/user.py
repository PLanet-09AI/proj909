from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: str
    email: str
    is_admin: bool = False
    created_at: datetime = None