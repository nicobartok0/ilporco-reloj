class Marca:
    def __init__(self, mar:dict):
        self.fecha = mar['fecha']
        self.dia = mar['dia']
        self.sucursal = mar['sucursal']
        self.funcion = mar['funcion']
        self.legajo = mar['legajo']
        self.empleado = f'{mar['apellido']}, {mar['nombre']}'
        self.hs_ingreso = mar['hs_ingreso']
        self.f_ingreso = mar['f_ingreso']
        self.f_almuerzo_salida = ''
        self.f_almuerzo_entrada = ''
        self.hs_salida = mar['hs_salida']
        self.f_salida = mar['f_salida']
        self.novedad = mar['novedad']
        self.observaciones = mar['observaciones']
        # Análisis? qué va en análisis?