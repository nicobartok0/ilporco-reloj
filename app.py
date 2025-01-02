import dearpygui.dearpygui as dpg
from operador import Operador

# Crea un operador que manejará el procesamiento de los datos
operador = Operador()
# Función para actualizar la tabla de reloj
def actualizar_tabla():
    # Limpiamos la tabla antes de actualizarla
    rows = dpg.get_item_children(item='tabla_reloj', slot=1)
    for row in rows:
        dpg.delete_item(row)

    for marca in operador.marcas:
        with dpg.table_row(parent='tabla_reloj'):
            tar = operador.calcular_tardanza(marca)

            dpg.add_text(marca.fecha)
            dpg.add_text(marca.dia)
            dpg.add_text(marca.sucursal)
            dpg.add_text(marca.funcion)
            dpg.add_text(marca.n_empleado)
            dpg.add_text(marca.empleado)
            dpg.add_text(marca.hs_ingreso)
            if tar['tardanza_entrada']:
                dpg.add_text(marca.f_ingreso, color=[175,0,0])
            else:
                dpg.add_text(marca.f_ingreso)
            dpg.add_text(marca.f_almuerzo_salida)
            dpg.add_text(marca.f_almuerzo_entrada)
            dpg.add_text(marca.hs_salida)
            if tar['salida_temprana']:
                dpg.add_text(marca.f_salida, color=[175,0,0])
            else:
                dpg.add_text(marca.f_salida)
            dpg.add_text(marca.novedad)
            dpg.add_text(marca.observaciones)

# Función para actualizar la tabla de horas semanales
def actualizar_tabla_horas():
    # Limpiamos la tabla antes de actualizarla
    rows = dpg.get_item_children(item='tabla_reloj_semanal', slot=1)
    for row in rows:
        dpg.delete_item(row)

    for marca in operador.marcas_horas:
        with dpg.table_row(parent='tabla_reloj_semanal'):
            dpg.add_text(marca.n_empleado)
            dpg.add_text(marca.empleado)
            dpg.add_text(marca.sucursal)
            dpg.add_text(marca.año)
            dpg.add_text(marca.semana)
            dpg.add_text(marca.horas)
            
# Función que listará los precios con el filtro aplicado
def listar():
    filtros = {
        'fecha_inicio': dpg.get_value('w_fecha_inicio'),
        'fecha_fin': dpg.get_value('w_fecha_fin'),
        'sucursal': dpg.get_value('w_sucursal'),
        'n_empleado': dpg.get_value('w_n_empleado'),
        'novedad': dpg.get_value('w_novedad'),
        'nombre': dpg.get_value('w_nombre'),
        'funcion': dpg.get_value('w_funcion')
    }
    operador.obtener_marcas(filtros)
    operador.obtener_marcas_semanales(filtros)
    actualizar_tabla()
    actualizar_tabla_horas()

# Configuración inicial de la ventana principal
dpg.create_context()
dpg.create_viewport(title="Consolidado de Asistencia", width=1750, height=690)

with dpg.window(tag="MainWindow", label="Consolidación de Asistencia", width=1600, height=560, pos=(0,30), menubar=True):
    with dpg.group(horizontal=True, width=220, height=100):
        with dpg.group(horizontal=True, width=180, height=20):
            with dpg.group(horizontal=False, width=30, height=100):
                dpg.add_input_text(label='Desde el YYYY-MM-DD', width=30, tag='w_fecha_inicio')
                dpg.add_input_text(label='Hasta el YYYY-MM-DD', width=200, tag='w_fecha_fin')
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_combo(label='Sucursal', width=200, items=operador.obtener_sucursales(), tag='w_sucursal')
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_input_text(label='N° Empleado', width=40, tag='w_n_empleado')
                dpg.add_input_text(label='Nombre', width=300, tag='w_nombre')
                dpg.add_combo(label='Función', width=200, items=operador.obtener_funciones(), tag='w_funcion')
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_combo(label='Novedad', items=operador.obtener_novedades(), tag='w_novedad')
        with dpg.group(horizontal=True, width=200, height=100):
            with dpg.group(horizontal=False, width=200, height=100):
                with dpg.child_window():
                    dpg.add_checkbox(label='Sin Anomalías', default_value=True)
                    dpg.add_checkbox(label='Sin Fichada ni novedad', default_value=True)
                    dpg.add_checkbox(label='Fichada con novedad', default_value=True)
                    dpg.add_checkbox(label='Ingreso tarde', default_value=True)
                    dpg.add_checkbox(label='Almuerzo extendido', default_value=True)
                    dpg.add_checkbox(label='Salida temprana', default_value=True)
            with dpg.group(horizontal=False):
                with dpg.child_window():
                    dpg.add_button(label='Listar', callback= listar)
                    dpg.add_button(label='Reportes')            
        
            
    with dpg.tab_bar(label='Tabs'):
        with dpg.tab(label='Reloj particular'):                
            with dpg.group(horizontal=False,width=1620, height=500):
                with dpg.table(label='Tabla de reloj', tag='tabla_reloj', resizable=True, policy=dpg.mvTable_SizingStretchProp):
                    dpg.add_table_column(label='Fecha', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Día', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Sucursal', width_stretch=True, init_width_or_weight=2)
                    dpg.add_table_column(label='Función', width_stretch=True, init_width_or_weight=2)
                    dpg.add_table_column(label='N° Empleado')
                    dpg.add_table_column(label='Empleado', width_stretch=True, init_width_or_weight=3)
                    dpg.add_table_column(label='Hora ingreso')
                    dpg.add_table_column(label='F/ingreso')
                    dpg.add_table_column(label='F/almuerzo salida', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='F/almuerzo regreso', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Hora salida')
                    dpg.add_table_column(label='F/salida')
                    dpg.add_table_column(label='Novedad', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Observaciones', width_stretch=True, init_width_or_weight=2)
                    dpg.add_table_column(label='Análisis', width_stretch=True, init_width_or_weight=2)
        
        with dpg.tab(label='Horas semanales'):                
            with dpg.group(horizontal=False,width=1620, height=500):
                with dpg.table(label='Horas semanales', tag='tabla_reloj_semanal', resizable=True, policy=dpg.mvTable_SizingStretchProp):
                    dpg.add_table_column(label='n_empleado', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Nombre', width_stretch=True, init_width_or_weight=2)
                    dpg.add_table_column(label='Sucursal', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Año', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Semana', width_stretch=True, init_width_or_weight=1)
                    dpg.add_table_column(label='Horas trabajadas', width_stretch=True, init_width_or_weight=1)
                    
                    



# Configuración y visualización del viewport
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()
