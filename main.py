from LoadFile import *
from base.KB import *

if __name__ == '__main__':
    kb = KB()
    for i in range(1, 6):
        input_file('inputs//input{}.txt'.format(i), kb)
        output_file('outputs//output{}.txt'.format(i), toString(PL_resolution(kb)))