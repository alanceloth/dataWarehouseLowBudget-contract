from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    transaction_time: datetime
    ean: int
    product_name: str
    price: float
    store: int
    pos_number: int
    pos_system: str
    pos_version: float
    pos_last_maintenance: datetime
    operator: int
