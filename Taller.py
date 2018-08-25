class Tree(object):
	def __init__(self, left, right, label):
		self.left = left
		self.right = right
		self.label = label

def Vi(A,I):
	if A.right == None:
		return I[A.label]
	elif A.label == "~":
		if Vi(A.right, I) == True:
			return False
		else:
			return True
	elif A.label == "&":
		if Vi(A.left, I) == True and Vi(A.right, I) == True:
			return True
		else:
			return False
	elif A.label == "|":
		if Vi(A.left, I) == True or Vi(A.right, I) == True:
			return True
		else:
			return False
	elif A.label == ">":
		if Vi(A.left, I) == False or Vi(A.right, I) == True:
			return True
		else:
			return False

def Interps():
    letrasProposicionales = ['p', 'q', 'r'] # lista con las letras proposicionales
    interps = [] # lista todas las posibles interpretaciones (diccionarios)
    aux = {} # primera interpretacion
    for a in letrasProposicionales:
        aux[a] = 1 # inicializamos la primera interpretacion con todo verdadero
    interps.append(aux) # ... y la incluimos en interps
    for a in letrasProposicionales:
        interps_aux = [i for i in interps] # lista auxiliar de nuevas interpretaciones
        for i in interps_aux:
            aux1 = {} # diccionario auxiliar para crear nueva interpretacion
            for b in letrasProposicionales:
                if a == b:
                    aux1[b] = 1 - i[b] # Cambia el valor de verdad para b
                else:
                    aux1[b] = i[b] # ... y mantiene el valor de verdad para las otras letras
            interps.append(aux1) # Incluye la nueva interpretacion en la lista

def Equival(arb1, arb2):
    a = True
    for I in Interps():
        if Vi(arb1,I) != Vi(arb2,I):
            a = False
    return a
		
def Inorder(f):
	if f.right == None:
		return f.label,
	elif f.label == '~':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
	stack = []
	for c in A:
		if c == "&" or c == "|" or c == ">":
			arb = Tree(stack[-1], stack[-2], c)
			del stack[-1]
			del stack[-1]
			stack.append(arb)
		elif c == '~':
			arb = Tree(None, stack[-1], c)
			del stack[-1]
			stack.append(arb)
		else:
			stack.append(Tree(None, None, c))
	return stack[-1]


form = raw_input("Ingrese la formula, en notacion polaca inversa: ")
Arb = StringtoTree(form)
print ("Usted ha creado el arbol", Inorder(Arb))
print ("El valor de verdad del arbol es" + Vi(Arb,I))