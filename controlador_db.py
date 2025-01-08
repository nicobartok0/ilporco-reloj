import requests

class Controlador_DB:
    def __init__(self):
        self.api_route = 'http://127.0.0.1:5000'

    def test_conexion(self):
        pass

    def cambiar_ruta(self, ruta):
        self.api_route = ruta

    def obtener_sucursales(self):
        req = f'{self.api_route}/obtener_sucursales'
        response = requests.get(req, verify=False)
        return response.json()
    
    def obtener_novedades(self):
        req = f'{self.api_route}/obtener_novedades'
        response = requests.get(req, verify=False)
        return response.json()
    
    def obtener_funciones(self):
        req = f'{self.api_route}/obtener_funciones'
        response = requests.get(req, verify=False)
        return response.json()

    def obtener_marcas(self, filtros):
        req = f'{self.api_route}/marcas'
        try:
            response = requests.get(req, verify=False, json=filtros)
            res = response.json()
        except:
            res = False
        return res
        
    def obtener_marcas_semanales(self, filtros):
        req = f'{self.api_route}/marcas_horasxsemana'
        try:
            response = requests.get(req, verify=False, json=filtros)
            res = response.json()
        except:
            res = False
        return res
    
    def obtener_horas_totales_por_numero(self, filtros):
        #res = requests.get('http://127.0.0.1:5000/obtener_horas_totales_x_numero', json=filtros)
        req = f'{self.api_route}/obtener_horas_totales_x_numero'
        try:
            response = requests.get(req, verify=False, json=filtros)
            res = response.json()
        except:
            res = False
        return res
    
    def cargar_novedades_ficha(self, datos):
        req = f'{self.api_route}/cargar_novedades_por_ficha'
        try:
            response = requests.put(req, verify=False, json=datos)
            res = response.json()
        except:
            res = False
        return res
    
    def actualizar_novedad(self, id, novedad):
        data = {
            'id': id,
            'novedad': novedad
        }
        req = f'{self.api_route}/actualizar_novedad'
        try:
            response = requests.put(req, verify=False, json=data)
            res = response.json()
        except:
            res = False
        return res

    
    
