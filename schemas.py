from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class SaleBase(BaseModel):
    customer_name: str
    phone_model: str
    color: str
    storage_gb: int
    price: float
    sale_date: date
    store_location: str

class SaleCreate(SaleBase):
    pass

class SaleUpdate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    created_at: datetime

   
    model_config = {
        "from_attributes": True
    }


class SaleStats(BaseModel):
    total_sales: int
    total_revenue: float
    most_popular_model: Optional[str]
    average_price: Optional[float]
