from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    producto: str
    stock_actual: int
    umbral: int

alertas_db = [
    Alerta(id=1, producto="Camisa", stock_actual=5, umbral=10),
    Alerta(id=2, producto="Pantalones", stock_actual=3, umbral=5)
]

@router.get("/alerta", response_model=List[Alerta])
async def get_alertas():
    return alertas_db

@router.post("/alerta", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta

@router.get("/alerta/{alerta_id}", response_model=Alerta)
async def get_alerta(alerta_id: int):
    for alerta in alertas_db:
        if alerta.id == alerta_id:
            return alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.put("/alerta/{alerta_id}", response_model=Alerta)
async def update_alerta(alerta_id: int, updated_alerta: Alerta):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            alertas_db[index] = updated_alerta
            return updated_alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.delete("/alerta/{alerta_id}")
async def delete_alerta(alerta_id: int):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            del alertas_db[index]
            return {"message": "Alerta deleted"}
    raise HTTPException(status_code=404, detail="Alerta not found")
