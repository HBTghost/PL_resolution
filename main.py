from IO import *
from base.knowledge import *

if __name__ == '__main__':
    knowledge = Knowledge()
    for i in range(1, 6):
        input_file('inputs//input{}.txt'.format(i), knowledge)
        output_file('outputs//output{}.txt'.format(i), PL_resolution(knowledge))
