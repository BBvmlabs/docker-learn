from fastapi import APIRouter, Depends, status, Path
from fastapi.responses import JSONResponse, Response
from models.rdb import Product
from schema.rdb import RDInputSchema, RDOutputSchema, RDPUTSchema
from sqlalchemy.ext.asyncio import AsyncSession
from database.rdb import get_db
from sqlalchemy import select
from typing import List

router = APIRouter()

@router.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(data : RDInputSchema, db: AsyncSession = Depends(get_db)):

    new_product = Product(**data.model_dump())

    db.add(new_product)
    await db.commit()

    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Product Created Successsfully")

@router.get("/product", status_code= status.HTTP_200_OK, response_model= List[RDOutputSchema])
async def get_products(db:AsyncSession = Depends(get_db)):

    product_list = (await db.execute(select(Product))).scalars().all()

    return product_list

@router.get("/product/{id}", status_code=status.HTTP_200_OK, response_model=RDOutputSchema)
async def get_product(id : int = Path(), db : AsyncSession = Depends(get_db)):

    product = (await db.execute(select(Product).where(Product.id==id))).scalar()

    return product

@router.put("/product/{id}", status_code=status.HTTP_200_OK, response_model=RDOutputSchema)
async def get_product(data: RDPUTSchema, id : int = Path()  ,db : AsyncSession = Depends(get_db)):

    product = (await db.execute(select(Product).where(Product.id==id))).scalar()

    product.name = data.name
    product.description = product.description
    product.price = data.price
    product.stock_in = data.stock_in
    product.seller = data.seller
    
    return product

@router.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def get_product(id : int = Path(), db : AsyncSession = Depends(get_db)):

    product = (await db.execute(select(Product).where(Product.id==id))).scalar()

    await db.delete(product)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)