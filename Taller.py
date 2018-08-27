#-*-coding: utf-8-*-

#Miguel Valencia Z y Nicolás Rojas

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    if f.right == None:
        print f.label,
    elif f.label == '-':
        print f.label,
        Inorder(f.right)
    else:
        print "(",
        Inorder(f.left)
        print f.label,
        Inorder(f.right)
        print ")",



def Vi(A,I):
	if A.right == None:
		return I[A.label]
	elif A.label == "-":
		if Vi(A.right, I):
			return False
		else:
			return True
	elif A.label == "Y":
		if Vi(A.left, I) and Vi(A.right, I):
			return True
		else:
			return False
	elif A.label == "O":
		if Vi(A.left, I) or Vi(A.right, I):
			return True
		else:
			return False
	elif A.label == ">":
		if not Vi(A.left, I) or Vi(A.right, I):
			return True
		else:
			return False

def Interps():
	letrasProposicionales = ['p', 'q', 'r','t','s']
	interps = []
	aux = {}
	for a in letrasProposicionales:
		aux[a] = True
	interps.append(aux)
	for a in letrasProposicionales:
		interps_aux = [i for i in interps]
		for i in interps_aux:
			aux1 = {}
			for b in letrasProposicionales:
				if a == b:
					aux1[b] = not i[b]
				else:
					aux1[b] = i[b]
			interps.append(aux1)
	return interps

def Equival(arb1, arb2, I):
	a = True
	for x in I:
		if Vi(arb1, x) != Vi(arb2,x):
			a = False
			break
	return a

def StringtoTree(A):
    letrasProposicionales = ['p', 'q', 'r', 's', 't', 'v']
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)
    return pila[-1]

#Ejercicio 5 (d)
cad = list('qp>')
cad2 = list('qp-O')
i = Interps()
form = StringtoTree(cad)
form2 = StringtoTree(cad2)
print u"fórmula 1: ", Inorder(form)
print u"fórmula 2:", Inorder(form2)
print u"Las dos fórmulas son equivalentes? ", Equival(form, form2, i)
print "\n"
print "-------------------------------------------------------------"+'\n'

#Ejercicio 5 (a)
cad3 = list('rqOpY')
cad4 = list('rpYqpYO')
form3 = StringtoTree(cad3)
form4 = StringtoTree(cad4)
print u"fórmula 3: ", Inorder(form3)
print u"fórmula 4:", Inorder(form4)
print u"Las dos fórmulas son equivalentes? ", Equival(form3, form4, i)
print "\n"
print "-------------------------------------------------------------"+'\n'

#Ejercicio 5 (b)
cad5 = list('qpO')
cad6 = list('q-p-Y-')
form5 = StringtoTree(cad5)
form6 = StringtoTree(cad6)
print u"fórmula 5: ", Inorder(form5)
print u"fórmula 6:", Inorder(form6)
print u"Las dos fórmulas son equivalentes? ", Equival(form5, form6, i)
print "\n"
print "-------------------------------------------------------------"+'\n'

#Ejercicio 5 (c)
cad7 = list('qpY')
cad8 = list('q-p-O-')
form7 = StringtoTree(cad7)
form8 = StringtoTree(cad8)
print u"fórmula 7: ", Inorder(form7)
print u"fórmula 8:", Inorder(form8)
print u"Las dos fórmulas son equivalentes? ", Equival(form7, form8, i)
print "\n"
print "-------------------------------------------------------------"+'\n'

#Ejercicio equivalente al 10% del taller: 
a=[]
cad9 = list('tsrOqp>->Y')
form9 = StringtoTree(cad9)
for i in Interps():
    if Vi(form9,i):
        a.append(i)
print u"Todas las interpretaciones que hacen verdadera a la fórmula ", Inorder(form9)
print u" son: "+'\n'+'\n', a
