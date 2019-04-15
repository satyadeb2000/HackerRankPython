for t in range(input()):
    input()
    lst = map(int, input().split())
    l = len(lst)
    i = 0
    #the smallest number has to be in the middle
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print(["Yes" if i == l - 1 else "No"])