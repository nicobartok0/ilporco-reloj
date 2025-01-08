from lector import Lector

lector = Lector()

novedades = lector.obtener_novedades('novedades.xlsx')

print(novedades)

for key in novedades.keys():
    print(f'Elementos de {key}:')
    for fecha in novedades[key].keys():
        print(fecha)
        print(f'\t{novedades[key][fecha]}')