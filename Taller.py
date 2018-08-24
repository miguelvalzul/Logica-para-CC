class Tree(object):
	def __init__(self, left, right, label):
		self.left = left
		self.right = right
		self.label = label

def Vi(A):
	if A.right == None:
		return I(A.label)
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
		
I = {"p": True, "q": True, "r": False}
