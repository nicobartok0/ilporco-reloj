import requests
filtros = {
        'fecha_inicio': '',
        'fecha_fin': '',
        'sucursal': '',
        'n_empleado': '',
        'novedad': '',
        'nombre': 'SACCA',
        'funcion': ''
    }
res = requests.get('http://127.0.0.1:5000/marcas_horasxsemana', json=filtros)
print(res.json())