class Tree(object):
	def __init__(self, left, right, label):
		self.left = left
		self.right = right
		self.label = label

def Vi(A,I):
	if A.right == None:
		return I[A.label]
	elif A.label == "~":
		if Vi(A.right) == True:
			return False
		else:
			return True
	elif A.label == "&":
		if Vi(A.left) == True and Vi(A.right) == True:
			return True
		else:
			return False
	elif A.label == "|":
		if Vi(A.left) == True or Vi(A.right) == True:
			return True
		else:
			return False
	elif A.label == "->":
		if Vi(A.left) == False or Vi(A.right) == True:
			return True
		else:
			return False
	elif A.label == "<->":
		if Vi(A.left) == Vi(A.right):
			return True
		else:
			return False

def Interps():
	letrasProposicionales = ['p', 'q', 'r']
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
	for x in I():
		if Vi(arb1, x) != Vi(arb2,x):
			a = False
			break
	return a
		
def Inorder(A):
	if A.right == None:
		return A.label,
	elif A.label == '~':
		return A.label + Inorder(A.right)
	else:
		return "(" + Inorder(A.left) + A.label + Inorder(A.right) + ")"

def StringtoTree(A):
	stack = []
	for c in A:
		if c == "&" or c == "|" or c == "->" or c == "<->":
			arb = Tree(stack[-1], stack[-2], c)
			del stack[-1]
			del stack[-1]
			stack.append(aux)
		elif c == '~':
			arb = Tree(None, stack[-1], c)
			del stack[-1]
			stack.append(arb)
		else:
			stack.append(Tree(None, None, c))
	return stack[-1]


form = raw_input("Ingrese la primera formula, en notacion polaca inversa: ")
Arb1 = StringtoTree(form)
print ("Usted ha creado la formula", Inorder(Arb1))
form = raw_input("Ingrese la segunda formula, en notacion polaca inversa: ")
Arb2 = StringtoTree(form)
print ("Usted ha creado la formula", Inorder(Arb2))
i = Interps()
if Equival(Arb1, Arb2, i):
	print "Las dos formulas son equivalentes"
else:
	print "Las dos formulas no son equivalentes"
