import requests


class Controlador_DB:
    def __init__(self):
        self.API_ROUTE = 'http://127.0.0.1:5000'

    def obtener_sucursales(self):
        req = f'{self.API_ROUTE}/obtener_sucursales'
        response = requests.get(req, verify=False)
        return response.json()
    
    def obtener_novedades(self):
        req = f'{self.API_ROUTE}/obtener_novedades'
        response = requests.get(req, verify=False)
        return response.json()
    
    def obtener_funciones(self):
        req = f'{self.API_ROUTE}/obtener_funciones'
        response = requests.get(req, verify=False)
        return response.json()
    

    def obtener_marcas(self):
        req = f'{self.API_ROUTE}/listar_horas_totales_empleado'
        response = requests.get(req, verify=False)
        return response.json()
    
