from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Bill(BaseModel):
    id: str
    title: str
    status: str
    introduced_date: datetime
    summary: Optional[str] = None

class Member(BaseModel):
    id: str
    name: str
    party: str
    state: str
    title: str
    bill_sponsorship: List[str]  # List of Bill IDs
