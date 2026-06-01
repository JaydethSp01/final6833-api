from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str

productos_db = [
    Producto(id=1, nombre="Camisa", precio=29.99, categoria="Ropa"),
    Producto(id=2, nombre="Pantalones", precio=49.99, categoria="Ropa")
]

@router.get("/producto", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.post("/producto", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.get("/producto/{producto_id}", response_model=Producto)
async def get_producto(producto_id: int):
    for producto in productos_db:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.put("/producto/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, updated_producto: Producto):
    for index, producto in enumerate(productos_db):
        if producto.id == producto_id:
            productos_db[index] = updated_producto
            return updated_producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/producto/{producto_id}")
async def delete_producto(producto_id: int):
    for index, producto in enumerate(productos_db):
        if producto.id == producto_id:
            del productos_db[index]
            return {"message": "Producto deleted"}
    raise HTTPException(status_code=404, detail="Producto not found")
