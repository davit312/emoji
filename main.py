from itertools import count
from emoji import *

count = 0
for i in emoji:
    count += 1
    char = i[0]
    print( f"{char:<5} => {i[1]:^30},\t len: {len(char)} | " , end="")
    for c in char:
        print(str(f"{ord(c):x} "),  end="")
    print()
    if count % 100 == 0:
        print('----',count,'---')
        input("=============== =============== ============== =======")
