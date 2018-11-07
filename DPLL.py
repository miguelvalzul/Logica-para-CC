from random import choice

class Tree(object):
    def __init__(self, r, iz, der):
        self.left = iz
        self.right = der
        self.label = r

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
            aux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(aux)
        elif c in conectivos:
            aux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(aux)
    return pila[-1]

def quitarDobleNegacion(f):
    # Elimina las dobles negaciones en una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: tree sin dobles negaciones

    if f.right == None:
        return f
    elif f.label == '-':
        if f.right.label == '-':
            return quitarDobleNegacion(f.right.right)
        else:
            return Tree('-', None, quitarDobleNegacion(f.right))
    else:
        return Tree(f.label, quitarDobleNegacion(f.left), quitarDobleNegacion(f.right))

def reemplazarImplicacion(f):
    # Regresa la formula reemplazando p>q por -pOq
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

    if f.right == None:
        return f
    elif f.label == '-':
        return Tree('-', None, reemplazarImplicacion(f.right))
    elif f.label == '>':
        noP = Tree('-', None, reemplazarImplicacion(f.left))
        Q = reemplazarImplicacion(f.right)
        return Tree('O', noP, Q)
    else:
        return Tree(f.label, reemplazarImplicacion(f.left), reemplazarImplicacion(f.right))

def deMorgan(f):
    # Regresa la formula aplicando deMorgan -(pYq) por -pO-q
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

    if f.right == None:
        return f
    elif f.label == '-':
        if f.right.label == 'Y':
            return Tree('O', Tree('-', None, deMorgan(f.right.left)), Tree('-', None, deMorgan(f.right.right)))
        elif f.right.label == 'O':
            return Tree('Y', Tree('-', None, deMorgan(f.right.left)), Tree('-', None, deMorgan(f.right.right)))
        else:
            return Tree('-', None, deMorgan(f.right))
    else:
        return Tree(f.label, deMorgan(f.left), deMorgan(f.right))

def distributiva(f):
    # Distribuye O sobre Ys: convierte rO(pYq) en (rOp)Y(rOq)
    # Input: tree, que es una formula de logica proposicional
    # Output: tree

    if f.right == None:
        return False, f
    elif f.label == 'O':
        if f.left.label == 'Y':
            P = f.left.left
            Q = f.left.right
            R = f.right
            return True, Tree('Y', Tree('O', P, R), Tree('O', Q, R))
        if f.right.label == 'Y':
            R = f.left
            P = f.right.left
            Q = f.right.right
            return True, Tree('Y', Tree('O', R, P), Tree('O', R, Q))
        else:
            cambioIz, Iz = distributiva(f.left)
            cambioDer, Der = distributiva(f.right)
            return cambioIz or cambioDer, Tree(f.label, Iz, Der)
    elif f.label == '-':
        cambio, hijo = distributiva(f.right)
        return cambio, Tree('-', None, hijo)
    else:
        cambioIz, Iz = distributiva(f.left)
        cambioDer, Der = distributiva(f.right)
        return cambioIz or cambioDer, Tree(f.label, Iz, Der)

def eliminaConjunciones(f):
    # Devuelve una lista de disyunciones de literales
    # Input: tree, que es una formula en CNF
    # Output: lista de cadenas
    if f.right == None:
        a = [Inorder(f)]
        return a
    elif f.label == 'O':
        return [Inorder(f)]
    elif f.label == 'Y':
        a = eliminaConjunciones(f.left)
        b = eliminaConjunciones(f.right)
        return a + b
    else:
        if f.label == '-':
            if f.right.right == None:
                return [Inorder(f)]

def complemento(l):
    # Devuelve el complemento de un literal
    # Input: l, que es una cadena con un literal (ej: p, -p)
    # Output: l complemento
    if '-' in l:
        return l[1:]
    else:
        return '-' + l

def formaClausal(f):
    # Obtiene la forma clausal de una formula en CNF
    # Input: tree, que es una formula de logica proposicional en CNF
    # Output: lista de clausulas

    f = quitarDobleNegacion(f)
    f = reemplazarImplicacion(f)
    f = quitarDobleNegacion(f)

    while True:
        g = deMorgan(f)
        g = quitarDobleNegacion(g)
        if  Inorder(f) != Inorder(g):
            f = g
        else:
            break

    while True:
        cambio, g = distributiva(f)
        if cambio:
            f = g
        else:
            break

    aux = eliminaConjunciones(f)
    badChars = ['(', ')']
    conjuntoClausulas = []
    for C in aux:
        C = ''.join([x for x in C if x not in badChars])
        C = C.split('O')
        conjuntoClausulas.append(C)

    aux = []
    for C in conjuntoClausulas:
        trivial = False
        for x in C:
            xComplemento = complemento(x)
            if xComplemento in C:
                trivial = True
                break
        if not trivial:
            aux.append(C)

    # Eliminamos repeticiones dentro de cada clausula
    aux = [list(set(i)) for i in aux]
    # Eliminamos clausulas repetidas
    aux_set = set(tuple(x) for x in aux)
    aux = [list(x) for x in aux_set]
    conjuntoClausulas = aux
    return conjuntoClausulas

def unitPropagation(S, I):
    # Algoritmo para eliminar clausulas unitarias de un conjunto de clausulas, manteniendo su satisfacibilidad
    # Input: Conjunto de clausulas S, interpretacion I (diccionario literal->True/False)
    # Output: Conjunto de clausulas S, interpretacion I (diccionario literal->True/False)

    while [] not in S:
        unit = ""
        for x in S:
            if len(x) == 1:
                unit = x[0]
                break
        if len(unit) == 0:
            break
        complement = complemento(unit)
        for x in S:
            if unit in x:
                S.remove(x)
            elif complement in x:
                x.remove(complement)
        if '-' in unit:
            I[complement] = False
        else:
            I[unit] = True
    return S, I

def DPLL(S, I):
    # Algoritmo para verificar la satisfacibilidad de una formula, y encontrar un modelo de la misma
    # Input: Conjunto de clausulas S, interpretacion I (diccionario literal->True/False)
    # Output: String Satisfacible/Insatisfacible, interpretacion I (diccionario literal->True/False)

    S, I = unitPropagation(S, I)
    if len(S) == 0:
        return "Satisfacible", I
    if [] in S:
        return "Insatisfacible", {}
    literales = []
    for x in S:
        for y in x:
            if y not in literales:
                literales.append(y)
    literal = choice(literales)
    complement = complemento(literal)
    newS = [y for y in S if literal not in y]
    for z in newS:
        if complement in z:
            z.remove(complement)
    newI = I
    if '-' in literal:
        newI[complement] = False
    else:
        newI[literal] = True
    sat, newI = DPLL(newS, newI)
    if sat == "Satisfacible":
        return sat, newI
    else:
        newS = [y for y in S if complement not in y]
        for z in newS:
            if literal in z:
                z.remove(literal)
        newI = I
        if '-' in complement:
            newI[literal] = False
        else:
            newI[complement] = True
        return DPLL(newS, newI)