from __future__ import print_function
from collections import deque

if __name__ == "__main__":
    myQueue = deque()
    for _ in range(int(input())):
        inp = input().split()
        getattr(myQueue, inp[0])(*[inp[1]] if len(inp) > 1 else [])

    print(*[item for item in myQueue])
        

    
        
 
        