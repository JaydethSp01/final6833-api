from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.routers import producto, categoria, proveedor, stock
app = FastAPI()
origins = os.environ.get("CORS_ORIGINS", "*").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(producto.router)
app.include_router(categoria.router)
app.include_router(proveedor.router)
app.include_router(stock.router)
@app.get("/health")
async def health_check():
    return {"status": "ok"}
