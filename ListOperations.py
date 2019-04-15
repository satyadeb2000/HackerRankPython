if __name__ == '__main__':
    N = int(input("Enter number of commands: "))
    myList = []

    for _ in range(N):
        inp = input("Enter Command: ").split()
        if inp[0] == "print":
            print(myList)
        else:
            if len(inp) == 2:
                getattr(myList, inp[0])(*[int(inp[1])])
            elif len(inp) == 3:
                getattr(myList, inp[0])(*[int(inp[1]), int(inp[2])])
            else:
                getattr(myList, inp[0])()
        

        
