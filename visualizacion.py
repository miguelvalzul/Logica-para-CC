#-*-coding: utf-8-*-
# Miguel Valencia y Nicolás Rojas, Octubre 2018

# Visualizacion de cuatro puertas de madera a partir de
# una lista de literales. Cada literal representa una sola puerta;
# el literal es positivo sii hay un diploma oculto detrás de la puerta en cuestión.

# Formato de la entrada: - las letras proposionales seran: 1, 2, 3, 4;
#                        - solo se aceptan literales (ej. 1, -2, 3, -4, etc.)

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
    arr_img = plt.imread("puertaED.png", format='png')
    imagebox1 = OffsetImage(arr_img, zoom=0.4)
    imagebox1.image.axes = axes
    
    arr_img = plt.imread("puertaCD.png", format='png')
    imagebox2 = OffsetImage(arr_img, zoom=0.4)
    imagebox2.image.axes = axes
    
    arr_img = plt.imread("puertaD.png", format='png')
    imagebox3 = OffsetImage(arr_img, zoom=0.4)
    imagebox3.image.axes = axes
    
    arr_img = plt.imread("puertaRD.png", format='png')
    imagebox4 = OffsetImage(arr_img, zoom=0.4)
    imagebox4.image.axes = axes
    
    arr_img = plt.imread("puertaEM.png", format='png')
    imagebox5 = OffsetImage(arr_img, zoom=0.4)
    imagebox5.image.axes = axes
    
    arr_img = plt.imread("puertaCM.png", format='png')
    imagebox6 = OffsetImage(arr_img, zoom=0.4)
    imagebox6.image.axes = axes
    
    arr_img = plt.imread("puertaM.png", format='png')
    imagebox7 = OffsetImage(arr_img, zoom=0.4)
    imagebox7.image.axes = axes
    
    arr_img = plt.imread("puertaRM.png", format='png')
    imagebox8 = OffsetImage(arr_img, zoom=0.4)
    imagebox8.image.axes = axes

    
    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.13, 0.467]
    direcciones[2] = [0.37, 0.467]
    direcciones[3] = [0.62, 0.467]
    direcciones[4] = [0.88, 0.467] 
                                                                


    ab = AnnotationBbox(imagebox5, direcciones[1], frameon=False)
    ab2 = AnnotationBbox(imagebox6, direcciones[2], frameon=False)
    ab3 = AnnotationBbox(imagebox7, direcciones[3], frameon=False)
    ab4 = AnnotationBbox(imagebox8, direcciones[4], frameon=False)
    axes.add_artist(ab)
    axes.add_artist(ab2)
    axes.add_artist(ab3)
    axes.add_artist(ab4)
    
    for l in f:
        if '-' not in l:
            num = 0
            if "1" in l:
                num = 1
            elif "2" in l:
                num = 2
            elif "3" in l:
                num = 3
            elif "4" in l:
                num = 4
            dip = AnnotationBbox(eval("imagebox"+str(num)), direcciones[num], frameon=False)
            axes.add_artist(dip)

    # plt.show()
    fig.savefig("puertas_" + str(n) + ".png")


#################
# importando paquetes para dibujar
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
#from sys import argv

#script, data_archivo = argv

#with open(data_archivo) as csv_file:
#    data = csv.reader(csv_file, delimiter=',')
#    contador = 1
#    for l in data:
#        print "Dibujando puertas:", l
#        dibujar_puertas(l, contador)
#        contador += 1