from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text,Optional
from datetime import datetime
from uuid import UUID as cc
from routes.routes import User


app = FastAPI()
app.include_router(User)


#Post Model
class Creacion_de_factura(BaseModel):
    id: cc
    Nombre_usuario: str
    Numero_factura: str
    TipoDeLectura: Text
    Fecha_factura: datetime = datetime.now()
    Subtotal: str
    Iva: str
    Total: str

    #valor: 
    # diponible: 
    

@app.get("/")
def read_root():
    return {"messege": "Bienvenido a su libreria favorita"}

@app.post("/facturacion")
def Creacion_de_factura(facturacion:Creacion_de_factura):
    return "recibido"

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
    return {"user_id" : user_id}
    
busqueda = [{"busqueda": "precios"},{"busqueda:": "lista de compras"},{"busqueda:": "facturas"},
{"busqueda:": "libros"},{"busqueda:": "orden de compra"}]

@app.get("/busqueda/")
async def read_item(skip: int = 0, limit: int = 10):
    return busqueda[skip : skip + limit]

titulos = [{"titulos": "aventura"},{"titulos": "ficcion"},{"titulos": "ciencia"},
{"titulos": "romance"},{"titulos": "drama"},{"titulos": "ciencia ficcion"},{"titulos": "terror"}]

@app.get("/titulos")
async def read_item(skip: int = 0, limit: int = 10):
    return titulos[skip : skip + limit]

