from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from consultas import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite cualquier origen (dominio)
    allow_credentials=False,  # ¡ATENCIÓN! Debe ser False si usas "" en origins, si usa usuario y contraseña, tendrá que ser true
    allow_methods=["*"],      # Permite todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],      # Permite todas las cabeceras HTTP
)

class ModelMovimiento(BaseModel):
    date: str
    concept: str
    quantity: float


@app.get('/movimientos', tags = ['Movimiento'])
def index():
    return select_all()

@app.get('/movimientos/{id}', tags = ['Movimiento'])
def movimientos_by_id(id:int):
    return select_by_id(id)

@app.post('/movimientos', tags=['Movimiento'])
def movimiento_registro(body: ModelMovimiento):
    try:
        insert_data([body.date, body.concept, body.quantity])
        return {'registro': 'correcto'}

    except Exception as ex:
        print(ex)
        return {'error': 'ha fallado el registro'}

@app.put('/movimientos/{id}', tags = ['Movimiento'])
def movimiento_update(id:int,body:ModelMovimiento):
    try:
        update_data(id,[body.date, body.concept, body.quantity])
        return {'registro ': 'actualizado correctamente'}

    except Exception as ex:
        print(ex)
        return {'error': ' ha fallado la actualización'}

@app.delete('/movimientos/{id}', tags=['Movimiento'])
def movimiento_borrado(id:int):
    try:
        delete_data(id)
        return {'registro' : ' eliminado correctamente'}

    except Exception as ex:
        print(ex)
        return {'ha fallado': ' el borrado'}

@app.get('/movimientos/ingresos', tags= ['Movimiento'])
def movimiento_ingresos():
    return mostrar_ingresos()

@app.get('/movimientos/gastos', tags=['Movimiento'])
def movimiento_gastos():
    return mostrar_gastos()