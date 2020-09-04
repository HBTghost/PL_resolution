from base.algorithms import *
from base.knowledge import *

def extract(line):
    res = []
    for s in line.strip().split(' '):
        if s != 'OR' and s != '':
            res.append(s)
    return res

def to_string(output):
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

def input_file(filename, knowledge):
    num_alpha, alpha = 0, []
    num_kb, KB = 0, []
    try:
        with open(filename, mode='r') as fi:
            lines = fi.readlines()
            num_alpha = int(lines[0])
            num_kb = int(lines[1 + num_alpha])
            alpha = [extract(lines[1 + i]) for i in range(num_alpha)]
            KB = [extract(lines[1 + num_alpha + 1 + i]) for i in range(num_kb)]
        knowledge.setKnowledge(KB, alpha)
        fi.close()
    except:
        pass

def output_file(filename, output):
    try:
        with open(filename, mode='w') as fo:
            fo.write(to_string(output))
        fo.close()
    except:
        pass
