from __future__ import print_function
from collections import deque

if __name__ == "__main__":
    resultqueue = deque()
    for _ in range(int(input("Enter the number of test cases :"))):
        Length = input("Enter the number of cubes: ")
        Cubes = list(str(input("Enter the Cube lengths: ")).split(sep = " "))
        myqueue = deque(Cubes)
        pilledUp = deque()
        result = "Yes"
        while len(myqueue) > 0:
            element1 = (int(myqueue.popleft()) if len(myqueue) > 0 else -1)
            element2 = (int(myqueue.pop()) if len(myqueue) > 0 else -1)
            element3 = (int(pilledUp.popleft()) if len(pilledUp) > 0 else -1)
            if (element3 == -1): #empty Queue
                if(element1 > element2):
                    pilledUp.appendleft(element1)
                    if element2 != -1:
                        myqueue.append(element2)
                elif(element2 > element1):
                    pilledUp.appendleft(element2)
                    if element1 != -1:
                        myqueue.appendleft(element1)
                else:
                    pilledUp.appendleft(element1)
                    pilledUp.appendleft(element2)
            else: #filled up queue
                if (element1 > element2) and (element1 <= element3):
                    #pop in element 1
                    pilledUp.appendleft(element3)
                    pilledUp.appendleft(element1)
                    if element2 != -1:
                        myqueue.append(element2)
                elif(element2 > element1) and (element2 <= element3): 
                    # pop in element 2
                    pilledUp.appendleft(element3)
                    pilledUp.appendleft(element2)
                    if element1 != -1:
                        myqueue.appendleft(element1)
                elif(element1 == element2) and (element2 <= element3):
                    pilledUp.appendleft(element3)
                    pilledUp.appendleft(element2)
                    pilledUp.appendleft(element1)
                else:
                    result = "No"
        resultqueue.append(result)
    
    for item in resultqueue:
        print(item)
                
            

            


