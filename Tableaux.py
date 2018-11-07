from random import choice

##############################################################################
# Definicion de objeto tree y funciones
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    return pila[-1]

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def obtiene_literales(cadena, letrasProposicionales):
	literales = []
	contador = 0
	while contador < len(cadena):
		if cadena[contador] == '-':
			l = cadena[contador] + cadena[contador+1]
			literales.append(l)
			contador += 1
		elif cadena[contador] in letrasProposicionales:
			l = cadena[contador]
			literales.append(l)
		contador += 1
	return literales


def Tableaux(lista_hojas, letrasProposicionales):

	# Algoritmo de creacion de tableau a partir de lista_hojas

	# Input: - lista_hojas: lista de lista de formulas
	#			(una hoja es una lista de formulas)
	#		 - letrasProposicionales: lista de letras proposicionales del lenguaje

	# Output: - String: Satisfacible/Insatisfacible
	# 		  - interpretaciones: lista de listas de literales que hacen verdadera
	#			la lista_hojas

	marcas = ['x', 'o']
	interpretaciones = [] # Lista para guardar interpretaciones que satisfacen la raiz

	while any(x not in marcas for x in lista_hojas): # Verifica si hay hojas no marcadas

		# Hay hojas sin marcar
		# Crea la lista de hojas sin marcar
		hojas_no_marcadas = [x for x in lista_hojas if x not in marcas]
		# Selecciona una hoja no marcada
		hoja = choice(hojas_no_marcadas)

		# Busca formulas que no son literales
		formulas_no_literales = []
		for x in hoja:
			if x.label not in letrasProposicionales:
				if x.label != '-':
					formulas_no_literales.append(x)
					break
				elif x.right.label not in letrasProposicionales:
					formulas_no_literales.append(x)
					break

		if formulas_no_literales != []: # Verifica si hay formulas que no son literales
			# Selecciona una formula no literal
			f = choice(formulas_no_literales)
			if f.label == 'Y':
				hoja.remove(f) # Quita a f de la hoja
				A1 = f.left
				if  A1 not in hoja:
					hoja.append(A1) # Agrega A1
				A2 = f.right
				if  A2 not in hoja:
					hoja.append(A2) # Agrega A2
			elif f.label == 'O':
				hoja.remove(f) # Quita la formula de la hoja
				lista_hojas.remove(hoja) # Quita la hoja de la lista de hojas
				B1 = f.left
				if  B1 not in hoja:
					S1 = [x for x in hoja] + [B1] # Crea nueva hoja con B1
				lista_hojas.append(S1) # Agrega nueva hoja con B1
				B2 = f.right
				if B2 not in hoja:
					S2 = [x for x in hoja] + [B2] # Crea nueva hoja con B2
				lista_hojas.append(S2) # Agrega nueva hoja con B2
			elif f.label == '>':
				hoja.remove(f) # Quita la formula de la hoja
				lista_hojas.remove(hoja) # Quita la hoja de la lista de hojas
				noB1 = Tree('-', None, f.left)
				if  noB1 not in hoja:
					S1 = [x for x in hoja] + [noB1] # Crea nueva hoja con no B1
				lista_hojas.append(S1) # Agrega nueva hoja con no B1
				B2 = f.right
				if B2 not in hoja:
					S2 = [x for x in hoja] + [B2] # Crea nueva hoja con B2
				lista_hojas.append(S2) # Agrega nueva hoja con B2
			elif f.label == '-':
				if f.right.label == '-':
					hoja.remove(f) # Quita a f de la hoja
					A1 = f.right.right
					if A1 not in hoja:
						hoja.append(A1) # Agrega la formula sin doble negacion
				elif f.right.label == 'O':
					hoja.remove(f) # Quita a f de la hoja
					noA1 = Tree('-', None, f.right.left)
					if noA1 not in hoja:
						hoja.append(noA1) # Agrega no A1
					noA2 = Tree('-', None, f.right.right)
					if noA2 not in hoja:
						hoja.append(noA2) # Agrega no A2
				elif f.right.label == '>':
					hoja.remove(f) # Quita a f de la hoja
					A1 = f.right.left
					if A1 not in hoja:
						hoja.append(A1) # Agrega A1
					noA2 = Tree('-', None, f.right.right)
					if noA2 not in hoja:
						hoja.append(noA2) # Agrega no A2
				elif f.right.label == 'Y':
					hoja.remove(f) # Quita la formula de la hoja
					lista_hojas.remove(hoja) # Quita la hoja de la lista de hojas
					noB1 = Tree('-', None, f.right.left)
					if  noB1 not in hoja:
						S1 = [x for x in hoja] + [noB1] # Crea nueva hoja con no B1
					lista_hojas.append(S1) # Agrega nueva hoja con no B2
					noB2 = Tree('-', None, f.right.right)
					if  noB2 not in hoja:
						S2 = [x for x in hoja] + [noB2] # Crea nueva hoja con no B2
					lista_hojas.append(S2) # Agrega nueva hoja con no B2

		else: # No hay formulas que no sean literales
			lista = list(imprime_hoja(hoja))
			literales = obtiene_literales(lista, letrasProposicionales)
			hojaConsistente = True
			for l in literales: # Verificamos que no hayan pares complementarios en la hoja
				if '-' not in l: # Verifica si el literal es positivo
					if '-' + l in literales: # Verifica si el complementario esta en la hoja
						lista_hojas.remove(hoja)
						hojaConsistente = False
						break

				elif l[1:] in literales: # Verifica si el complementario esta en la hoja
						lista_hojas.remove(hoja)
						hojaConsistente = False
						break

			if hojaConsistente: # Se recorrieron todos los literales y no esta el complementario
				interpretaciones.append(hoja) # Guarda la interpretacion que satisface la raiz
				lista_hojas.remove(hoja)

	# Dice si la raiz es inconsistente
	if len(interpretaciones) > 0:
		# Interpreta como string la lista de interpretaciones
		INTS = []
		for i in interpretaciones:
			aux = [Inorder(l) for l in i]
			INTS.append(aux)

		# Eliminamos repeticiones dentro de cada interpretacion
		INTS = [list(set(i)) for i in INTS]
		# Eliminamos interpretaciones repetidas
		INTS_set = set(tuple(x) for x in INTS)
		INTS = [list(x) for x in INTS_set]

		return "Satisfacible", INTS
	else:
		return "Insatisfacible", None