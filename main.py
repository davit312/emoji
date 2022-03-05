from itertools import count
from emoji import *

lineTemplate = "{:<5} => {:^30},\t len: {} | "
count = 0
for i in emoji:
    count += 1
    char = i[0]
    print( lineTemplate.format(char,i[1], len(char)) , end="")
    for c in char:
        print("{:x} ".format(ord(c)),  end="")
    print()
    if count % 100 == 0:
        print('----',count,'---')
        input("=============== =============== ============== =======")
