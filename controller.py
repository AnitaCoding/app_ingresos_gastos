from fastapi import FastAPI
from pydantic import BaseModel

from consultas import *

app = FastAPI()

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
