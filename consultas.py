from conexion import Conexion
import sqlite3

def formato(respuesta):
    result = []
    for fila in respuesta.fetchall():
        result.append(dict(fila))
    return(result)

def select_all():
    conexion_select = Conexion('SELECT * FROM movimiento;')
    respuesta = conexion_select.res
    result = formato(respuesta)
    conexion_select.con.close()

    return result

def select_by_id(id: int):
    conexion_select_by = Conexion(f'SELECT * FROM movimiento WHERE id= {id}')
    respuesta = conexion_select_by.res
    result = formato(respuesta)
    conexion_select_by.con.close()
    return result

def insert_data(data: list):
    try:
        conexion_insert = Conexion('INSERT INTO movimiento(date, concept, quantity) VALUES (?,?,?);', data)          
        conexion_insert.res
        conexion_insert.con.commit()#para confirmar guardado
    except sqlite3.Error as error:
        print(error)
    conexion_insert.con.close()

def update_data(id, data):
    try:
        conexion_update = Conexion(f'UPDATE movimiento SET date=?, concept=?, quantity=? WHERE id={id};', data)
        conexion_update.res
        conexion_update.con.commit()
    except sqlite3.Error as error:
        print('Error update: ')
    conexion_update.con.close()

def delete_data(id):
    try:
        conexion_delete = Conexion(f'DELETE FROM movimiento WHERE id = {id}')
        conexion_delete.res
        conexion_delete.con.commit()
    except sqlite3.Error as error:
        print('Error delete: ', error)

def mostrar_ingresos():
    conexion_ingreso = Conexion('SELECT sum(quantity) FROM movimiento WHERE quantity < 0;')
    respuesta = conexion_ingreso.res
    resp = formato(respuesta)
    conexion_ingreso.con.close()
    return resp

def mostrar_gastos():
    conexion_gasto = Conexion('SELECT sum(quantity) FROM movimiento WHERE quantity > 0;')
    respuesta = conexion_gasto.res
    resp = formato(respuesta)
    conexion_gasto.con.close()
    return resp
