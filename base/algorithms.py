import copy
from itertools import product
from .KB import *

def negativeAlpha(alpha):
    negative = lambda x : x[1] if len(x) > 1 and x[0] == '-' else '-' + x
    distribution = lambda clauseA, clauseB : [a + b for a, b in product(clauseA, clauseB)]

    pre_neg = [[[negative(var)] for var in clause] for clause in alpha]
    res = pre_neg[0]
    for i in range(1, len(pre_neg)):
        res = distribution(res, pre_neg[i])

    return res

def is_neg(a, b):
    return a == '-' + b or b == '-' + a

def is_meaningless(clause):
    is_suck = lambda i, j : i != j and (clause[i] == clause[j] or is_neg(clause[i], clause[j]))
    size = len(clause)
    return size == 0 or any(is_suck(i, j) for i, j in product(range(size), repeat=2))

def is_stop(listClause):
    is_empty = lambda a, b : len(a) == 1 and len(b) == 1 and is_neg(a[0], b[0])
    return any(is_empty(a, b) for a, b in product(listClause, repeat=2))

def logic(clauseA, clauseB):
    A = copy.deepcopy(clauseA)
    B = copy.deepcopy(clauseB)
    for iA in range(len(A)):
        for iB in range(len(B)):
            if is_neg(A[iA], B[iB]):
                A.pop(iA)
                B.pop(iB)
                return True, A + B
    return False, A + B

def createNewList(listClause):
    is_same = lambda clauseA, clauseB : sorted(clauseA) == sorted(clauseB)
    is_exist = lambda clause, listClause : any(is_same(tmp, clause) for tmp in listClause)
    
    res, count = [], 0
    for i in range(len(listClause) - 1):
        for j in range(i + 1, len(listClause)):
            req, clause = logic(listClause[i], listClause[j])
            if req and not is_meaningless(clause) and not is_exist(clause, listClause + res):
                res.append(clause)
    return res

def PL_resolution(KB):
    sort_output = lambda output : [[sorted(clause, key=lambda x : x[1:] if x[0] == '-' else x) if type(clause) is not str else clause for clause in gr] if type(gr) is not str else gr for gr in output]

    output = []
    listClause = KB.getKb() + negativeAlpha(KB.getAlpha())
    listNewClause = createNewList(listClause)
    while (len(listNewClause) > 0):
        output.append(listNewClause)
        listClause += listNewClause
        listNewClause = createNewList(listClause)
        if is_stop(listClause):
            listNewClause.append('{}')
            output += [listNewClause, 'YES']
            return sort_output(output)
    output += [[], 'NO']
    return sort_output(output)


def toString(output):
    res = ''
    for x in output:
        if type(x) is not str:
            res += str(len(x)) + '\n'
            for y in x:
                if type(y) is not str:
                    for z in y:
                        res += z + ' OR '
                    res = res[:-4] + '\n'
                else:
                    res += y + '\n'
        else:
            res += x
    return res