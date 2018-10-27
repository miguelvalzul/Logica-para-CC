#-*-coding: utf-8-*-
# Miguel Valencia y Nicolás Rojas, Octubre 2018

# Codigo para crear la formula del problema de las puertas

import Tableaux

print("Creando formula...")

#Creacion de las letras proposicionales
#1 = El diploma esta detras de la puerta de ebano
#2 = El diploma esta detras de la puerta de caoba
#3 = El diploma esta detras de la puerta de cerezo
#4 = El diploma esta detras de la puerta de roble

letrasProposicionales = []
for i in range(1, 5):
    letrasProposicionales.append(str(i))

#Regla 1: Hay 8 afirmaciones sobre la ubicacion del diploma

afirmacionesIniciales = []
afirmacionesIniciales.append("1")
afirmacionesIniciales.append("2")
afirmacionesIniciales.append("4-")
afirmacionesIniciales.append("13O")
afirmacionesIniciales.append("14O-")
afirmacionesIniciales.append("12O")
afirmacionesIniciales.append("3-")
afirmacionesIniciales.append("2")

#Regla 2: De las 8 afirmaciones iniciales, hay exactamente 3 que son verdaderas. Las otras 5 son falsas

formula = ""

for a in range(len(afirmacionesIniciales)-2):
    for b in range(a+1, len(afirmacionesIniciales)-1):
        for c in range(b+1, len(afirmacionesIniciales)):
            posibleSolucion = afirmacionesIniciales[a]+afirmacionesIniciales[b]+"Y"+afirmacionesIniciales[c]+"Y"
            for d in afirmacionesIniciales:
                if d != afirmacionesIniciales[a] and d != afirmacionesIniciales[b] and d != afirmacionesIniciales[c]:
                    posibleSolucion += (d+"-Y")
            if len(formula) != 0:
                posibleSolucion += "O"
            formula += posibleSolucion

#Regla 3: Hay exactamente una puerta en la que se encuentra el diploma

regla3 = ""

for x in letrasProposicionales:
    posibleSolucion = x
    for y in letrasProposicionales:
        if x != y:
            posibleSolucion += (y + "-Y")
    if len(regla3) != 0:
        posibleSolucion += "O"
    regla3 += posibleSolucion


formula += (regla3 + "Y")

print("Implementando tableau...")

#Creacion de la formula como objeto

arbol = Tableaux.StringtoTree(formula, letrasProposicionales)

#Uso del algoritmo de los tableaux

satisfacibilidad, interpretaciones = Tableaux.Tableaux([[arbol]], letrasProposicionales)


if satisfacibilidad == 'Satisfacible':
    if len(interpretaciones) == 0:
        print ("Error: la lista de interpretaciones esta vacia")
    else:
        import csv
        archivo = 'puertas.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(interpretaciones)

        print ("Interpretaciones guardadas  en " + archivo)

        import visualizacion
        contador = 1
        for n in interpretaciones:
            visualizacion.dibujar_puertas(n,contador)
            contador += 1

print("Ejecucion finalizada")