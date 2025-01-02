from operador import Operador

operador = Operador()

filtros = {
        'fecha_inicio': '',
        'fecha_fin': '',
        'sucursal': '',
        'n_empleado': '',
        'novedad': '',
        'nombre': '',
        'funcion': ''
    }

operador.obtener_marcas(filtros=filtros)
for mov in operador.marcas:
    print(f'MOVIMIENTO {mov}')
    tar = operador.calcular_tardanza(mov)
    print(f'HORA ENTRADA: {mov.hs_ingreso}, FICHADO: {mov.f_ingreso}. TARDANZA? {tar['tardanza_entrada']}, de {tar['cant_tardanza']}')