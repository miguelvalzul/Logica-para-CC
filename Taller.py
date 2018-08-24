class Tree(object):
	def __init__(self, left, right, label):
		self.left = left
		self.right = right
		self.label = label

def Vi(A):
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
		if c == "&" or c == "|" or c == "->" or c == "<->":
			arb = Tree(c, stack[-1], stack[-2])
			del stack[-1]
			del stack[-1]
			stack.append(aux)
		elif c == '~':
			arb = Tree(c, None, stack[-1])
			del stack[-1]
			stack.append(arb)
		else:
			stack.append(Tree(c, None, None))

I = {"p": True, "q": True, "r": False}
