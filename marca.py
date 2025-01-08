class Marca:
    def __init__(self, mar:dict):
        self.id_marca = mar['id_marca']
        self.fecha = mar['fecha']
        self.dia = mar['dia']
        self.sucursal = mar['sucursal']
        self.funcion = mar['funcion']
        self.n_empleado = mar['n_empleado']
        self.empleado = f'{mar['apellido']}, {mar['nombre']}'
        self.hs_ingreso = self.format_fecha(mar['hs_ingreso'])
        self.f_ingreso = self.format_fecha(mar['f_ingreso'])
        if mar['inicio_almuerzo'] != None:
            self.f_almuerzo_salida = self.format_fecha(mar['inicio_almuerzo'])
        else:
            self.f_almuerzo_salida = None
        if mar['fin_almuerzo'] != None:
            self.f_almuerzo_entrada = self.format_fecha(mar['fin_almuerzo'])
        else:
            self.f_almuerzo_entrada = None
        self.hs_salida = self.format_fecha(mar['hs_salida'])
        self.f_salida = self.format_fecha(mar['f_salida'])
        self.hs_trabajadas = mar['horas_trabajadas']
        self.novedad = mar['novedad']
        self.observaciones = mar['observaciones']
        # Análisis? qué va en análisis?

    def format_fecha(self, fecha):
        if len(fecha) == 8:
            return fecha
        else:
            return f'0{fecha}'

class Marca_Semanal:
    def __init__(self, mar:dict):
        self.n_empleado = mar['n_empleado']
        self.empleado = f'{mar['apellido']}, {mar['nombre']}'
        self.sucursal = mar['sucursal']
        self.año = mar['año']
        self.semana = mar['semana']
        self.horas = mar['horas']

