import dearpygui.dearpygui as dpg
from operador import Operador

dpg.create_context()

operador = Operador()
operador.obtener_marcas(filtros={})


with dpg.window(label="Tutorial", width=500, height=500):
    dpg.add_simple_plot(label="Simpleplot2", default_value=(0.3, 0.9, 2.5, 8.9), overlay="Overlaying", height=180,
                        histogram=True)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()