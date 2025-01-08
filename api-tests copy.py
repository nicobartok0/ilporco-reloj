import requests
filtros = {
        'fecha_inicio': '',
        'fecha_fin': '',
        'sucursal': '',
        'n_empleado': '',
        'novedad': '',
        'nombre': '',
        'funcion': ''
    }
res = requests.get('http://127.0.0.1:5000/obtener_horas_totales_x_numero', json=filtros)
print(res.json())