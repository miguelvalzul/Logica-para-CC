class Tree(object):
	def __init__(self, left, right, label):
		self.left = left
		self.right = right
		self.label = label

def Vi(A,I):
	if A.right == None:
		return I[A.label]
	elif A.label == "~":
		if Vi(A.right, I):
			return False
		else:
			return True
	elif A.label == "&":
		if Vi(A.left, I) and Vi(A.right, I):
			return True
		else:
			return False
	elif A.label == "|":
		if Vi(A.left, I) or Vi(A.right, I):
			return True
		else:
			return False
	elif A.label == ">":
		if Vi(A.left, I) == False or Vi(A.right, I):
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
	for x in I:
		if Vi(arb1, x) != Vi(arb2,x):
			a = False
			break
	return a

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

form = raw_input("Ingrese la primera formula, en notacion polaca inversa: ")
Arb1 = StringtoTree(form)
form = raw_input("Ingrese la segunda formula, en notacion polaca inversa: ")
Arb2 = StringtoTree(form)
i = Interps()
if Equival(Arb1, Arb2, i):
	print "Las dos formulas son equivalentes"
else:
	print "Las dos formulas no son equivalentes"
