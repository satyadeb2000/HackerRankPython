from __future__ import print_function
for i in range(1,int(input())+1): 
    print(''.join(map(str, list(range(1,i+1)) + list(reversed(list(range(1,i)))))))


    
