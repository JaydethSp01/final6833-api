from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto: str
    talla: str
    cantidad: int

stocks_db = [
    Stock(id=1, producto="Camisa", talla="M", cantidad=50),
    Stock(id=2, producto="Pantalones", talla="L", cantidad=30)
]

@router.get("/stock", response_model=List[Stock])
async def get_stocks():
    return stocks_db

@router.post("/stock", response_model=Stock)
async def create_stock(stock: Stock):
    stocks_db.append(stock)
    return stock

@router.get("/stock/{stock_id}", response_model=Stock)
async def get_stock(stock_id: int):
    for stock in stocks_db:
        if stock.id == stock_id:
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.put("/stock/{stock_id}", response_model=Stock)
async def update_stock(stock_id: int, updated_stock: Stock):
    for index, stock in enumerate(stocks_db):
        if stock.id == stock_id:
            stocks_db[index] = updated_stock
            return updated_stock
    raise HTTPException(status_code=404, detail="Stock not found")

@router.delete("/stock/{stock_id}")
async def delete_stock(stock_id: int):
    for index, stock in enumerate(stocks_db):
        if stock.id == stock_id:
            del stocks_db[index]
            return {"message": "Stock deleted"}
    raise HTTPException(status_code=404, detail="Stock not found")
