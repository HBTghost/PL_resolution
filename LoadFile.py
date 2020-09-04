from base.algorithms import *
from base.KB import *

def extract(line):
    res = []
    for s in line.strip().split(' '):
        if s != 'OR' and s != '':
            res.append(s)
    return res

def input_file(filename, re_KB):
    num_alpha, alpha = 0, []
    num_kb, KB = 0, []
    try:
        with open(filename, mode='r') as fi:
            lines = fi.readlines()
            num_alpha = int(lines[0])
            num_kb = int(lines[1 + num_alpha])
            alpha = [extract(lines[1 + i]) for i in range(num_alpha)]
            KB = [extract(lines[1 + num_alpha + 1 + i]) for i in range(num_kb)]
        re_KB.setKB(alpha, KB)
        fi.close()
    except:
        pass

def output_file(filename, output):
    try:
        with open(filename, mode='w') as fo:
            fo.write(output)
        fo.close()
    except:
        pass
