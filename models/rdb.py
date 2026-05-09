from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, VARCHAR, Text
from database.rdb import Base

class Product(Base):
    __tablename__ = "Catagory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable= False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False, default= 0.0)
    stock_in = Column(Integer, nullable=False, default=0)
    seller = Column(String, nullable=False, default="")