import dearpygui.dearpygui as dpg
from operador import Operador

# Crea un operador que manejará el procesamiento de los datos
operador = Operador()

# Configuración inicial de la ventana principal
dpg.create_context()
dpg.create_viewport(title="Consolidado de Asistencia", width=1630, height=690)

with dpg.window(tag="MainWindow", label="Consolidación de Asistencia", width=1600, height=560, pos=(0,30), menubar=True):
    with dpg.group(horizontal=True, width=200, height=100):
        with dpg.group(horizontal=True, width=160, height=20):
            with dpg.group(horizontal=False, width=30, height=100):
                dpg.add_input_text(label='Desde el DD/MM/YYYY', width=30)
                dpg.add_input_text(label='Hasta el DD/MM/YYYY', width=200)
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_combo(label='Sucursal', width=200, items=operador.obtener_sucursales())
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_input_text(label='N° Empleado', width=40)
                dpg.add_input_text(label='Nombre', width=300)
                dpg.add_combo(label='Función', width=200, items=operador.obtener_funciones())
            with dpg.group(horizontal=False, width=260, height=100):
                dpg.add_combo(label='Novedad', items=operador.obtener_novedades())
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
                    dpg.add_button(label='Listar')
                    dpg.add_button(label='Reportes')            
        
            
                
    with dpg.group(horizontal=False,width=1600, height=500):
        with dpg.table(label='Tabla de reloj'):
            dpg.add_table_column(label='Fecha')
            dpg.add_table_column(label='Día')
            dpg.add_table_column(label='Sucursal')
            dpg.add_table_column(label='Función')
            dpg.add_table_column(label='Legajo')
            dpg.add_table_column(label='Empleado')
            dpg.add_table_column(label='Hora ingreso')
            dpg.add_table_column(label='F/ingreso')
            dpg.add_table_column(label='F/almuerzo salida')
            dpg.add_table_column(label='F/almuerzo regreso')
            dpg.add_table_column(label='Hora salida')
            dpg.add_table_column(label='F/salida')
            dpg.add_table_column(label='Novedad')
            dpg.add_table_column(label='Observaciones')
            dpg.add_table_column(label='Análisis')



# Configuración y visualización del viewport
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("MainWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()
