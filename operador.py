from controlador_db import Controlador_DB

class Operador:
    def __init__(self):
        self.db = Controlador_DB()

    def obtener_novedades(self):
        res = self.db.obtener_novedades()
        data = []
        for element in res:
            data.append(element['nombre_novedad'])
        return data
    
    def obtener_funciones(self):
        res = self.db.obtener_funciones()
        data = []
        for element in res:
            data.append(element['nombre_funcion'])
        return data
    
    def obtener_sucursales(self):
        res = self.db.obtener_sucursales()
        data = []
        for element in res:
            data.append(element['nombre'])
        return data
    