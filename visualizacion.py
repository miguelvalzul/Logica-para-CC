#-*-coding: utf-8-*-
# Miguel Valencia y Nicolás Rojas, Octubre 2018

# Visualizacion de cuatro puertas de madera a partir de
# una lista de literales. Cada literal representa una sola puerta;
# el literal es positivo sii hay un diploma oculto detrás de la puerta en cuestión.

# Formato de la entrada: - las letras proposionales seran: 1, 2, 3, 4;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)

# Salida: archivo puertas_%i.png, donde %i es un numero natural


def dibujar_puertas(f, n):
    # Visualiza un conjunto de cuatro puertas dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen puertas_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Cargando imagen de las puertas
    arr_img = plt.imread("puerta.png", format='png')
    imagebox1 = OffsetImage(arr_img, zoom=0.178)
    imagebox1.image.axes = axes

    # Cargando imagen de los monstruos
    arr_img = plt.imread("monstruo.png", format='png')
    imagebox2 = OffsetImage(arr_img, zoom=0.178)
    imagebox2.image.axes = axes
    
    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.333, 0.667]
    direcciones[2] = [0.667, 0.667]
    direcciones[3] = [0.333, 0.333]
    direcciones[4] = [0.667, 0.333]

    for l in f:
        if '~' in l:
            ab = AnnotationBbox(imagebox2, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)
        else:
            ab = AnnotationBbox(imagebox1, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)

    # plt.show()
    fig.savefig("puertas_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

script, data_archivo = argv

with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando puertas:", l
        dibujar_puertas(l, contador)
        contador += 1

csv_file.close()