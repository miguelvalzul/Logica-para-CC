#-*-coding: utf-8-*-
# Miguel Valencia y Nicolás Rojas, Octubre 2018

# Codigo para crear la formula del problema de las puertas

import DPLL

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

print("Implementando algoritmo DPLL...")

#Creacion de la formula como conjunto de clausulas

arbol = DPLL.StringtoTree(formula, letrasProposicionales)
clausulas = DPLL.formaClausal(arbol)

#Uso del algoritmo DPLL

satisfacibilidad, interps = DPLL.DPLL(clausulas, {})


if satisfacibilidad == 'Satisfacible':
    if len(interps) == 0:
        print ("Error: la lista de interpretaciones esta vacia")
    else:
        import csv
        archivo = 'puertas.csv'
        interpretaciones = []
        for i in interps:
            if interps[i]:
                interpretaciones.append(i)
            else:
                interpretaciones.append('-'+i)
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(interpretaciones)

        print ("Interpretaciones guardadas  en " + archivo)

        import visualizacion
        visualizacion.dibujar_puertas(interpretaciones, 1)

print("Ejecucion finalizada")