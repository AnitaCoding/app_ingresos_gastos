import sqlite3

class Conexion:
    def __init__(self, sql_query, param = []):
        self.con = sqlite3.connect("bd_ingresos_gastos.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.res = self.cur.execute(sql_query, param)
        