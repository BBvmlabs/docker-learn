from pydantic import BaseModel
from typing import Optional

class RDInputSchema(BaseModel):
    name: str
    description : str
    price : float
    stock_in : int
    seller : str

class RDPUTSchema(BaseModel):
    name: Optional[str]
    description : Optional[str]
    price : Optional[float]
    stock_in : Optional[int]
    seller : Optional[str]


class RDOutputSchema(BaseModel):
    id : int
    name: str
    description : str
    price : float
    stock_in : int
    seller : str