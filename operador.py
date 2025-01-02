from controlador_db import Controlador_DB
from marca import Marca, Marca_Semanal
from datetime import datetime, timedelta

class Operador:
    def __init__(self):
        self.db = Controlador_DB()
        self.dias = {
            1: 'Domingo',
            2: 'Lunes',
            3: 'Martes',
            4: 'Miércoles',
            5: 'Jueves',
            6: 'Viernes',
            7: 'Sábado'
        }
        self.marcas = []
        self.marcas_horas = []

    def obtener_novedades(self):
        res = self.db.obtener_novedades()
        data = ['']
        for element in res:
            data.append(element['nombre_novedad'])
        return data
    
    def obtener_funciones(self):
        res = self.db.obtener_funciones()
        data = ['']
        for element in res:
            data.append(element['nombre_funcion'])
        return data
    
    def obtener_sucursales(self):
        res = self.db.obtener_sucursales()
        data = ['']
        for element in res:
            data.append(element['nombre'])
        return data
    
    def obtener_marcas(self, filtros):
        try:
            res = self.db.obtener_marcas(filtros)
        except:
            print(Exception)
            self.marcas = []
            return self.marcas
        self.marcas = []
        if res != False:
            for element in res:
                mar = {
                    'fecha': element['fecha_marca'],
                    'dia': self.dias[element['dia']],
                    'sucursal': element['sucursal'],
                    'funcion': element['nombre_funcion'],
                    'n_empleado': element['num_empleado'],
                    'apellido': element['apellido'],
                    'nombre': element['nombre'],
                    'hs_ingreso': element['horario_entrada'],
                    'f_ingreso': element['hs_entrada'],
                    'inicio_almuerzo': element['inicio_almuerzo'],
                    'fin_almuerzo': element['fin_almuerzo'],
                    'hs_salida': element['horario_salida'],
                    'f_salida': element['hs_salida'],
                    'novedad': element['nombre_novedad'],
                    'observaciones': element['observaciones']
                }
                self.marcas.append(Marca(mar))

    def timedelta_to_str(self, tdelta):
        total_seconds = int(tdelta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"


    def calcular_tardanza(self, mov):
        delta_entrada = datetime.strptime(mov.f_ingreso, '%H:%M:%S') - datetime.strptime(mov.hs_ingreso, '%H:%M:%S') 
        delta_salida = datetime.strptime(mov.hs_salida, '%H:%M:%S') - datetime.strptime(mov.f_salida, '%H:%M:%S')
        tar = {
            'tardanza_entrada': False,
            'cant_tardanza': 0,
            'salida_temprana': False,
            'cant_temprana': 0
        }
        tolerancia = timedelta(minutes=15)
        if delta_entrada > tolerancia:
            tar['tardanza_entrada'] = True
            tar['cant_tardanza'] = self.timedelta_to_str(delta_entrada)

        if delta_salida > tolerancia:
            tar['salida_temprana'] = True
            tar['cant_temprana'] = self.timedelta_to_str(delta_salida)

        return tar
    
    def obtener_marcas_semanales(self, filtros):
        res = self.db.obtener_marcas_semanales(filtros)
        self.marcas_horas = []
        if res != False:
            for element in res:
                mar = {
                    'n_empleado': element['num_empleado'],
                    'nombre': element['nombre'],
                    'apellido': element['apellido'],
                    'sucursal': element['sucursal'],
                    'año': element['año'],
                    'semana': element['semana'],
                    'horas':element['horas_trabajadas']
                }
                self.marcas_horas.append(Marca_Semanal(mar=mar))