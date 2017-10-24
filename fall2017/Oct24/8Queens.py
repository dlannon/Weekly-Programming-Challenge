#Daniel Lannon
#8Queens

import sys


i=0
queens = []
        
for x in sys.stdin:
    l = x

check(l)

def check(q):
    for i in range(0,63):
        if q[i] == '*':
            for s in range(0,queens.length()):
                if q[i] - queens[s] % 7 == 0 or q[i] - queens[s] % 9 == 0 or q[i] % 8 == 0:
                    print("invalid")
                    return
            queens.append(q)
            
    

