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

    def obtener_marcas(self, filtros):
        req = f'{self.API_ROUTE}/marcas'
        try:
            response = requests.get(req, verify=False, json=filtros)
            res = response.json()
        except:
            res = False
        return res
        
    def obtener_marcas_semanales(self, filtros):
        req = f'{self.API_ROUTE}/marcas_horasxsemana'
        try:
            response = requests.get(req, verify=False, json=filtros)
            res = response.json()
        except:
            res = False
        return res
    
