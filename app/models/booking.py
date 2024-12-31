from dataclasses import dataclass
from datetime import datetime

@dataclass
class Booking:
    id: str
    user_id: str
    date: str
    time: str
    description: str
    status: str
    created_at: datetime