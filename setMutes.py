from __future__ import print_function
if __name__ == "__main__":
    Num = input()
    mySet = set(map(int, input().split()))
    for _ in range(int(input())):
        myInput = input().split()
        getattr(mySet, myInput[0])(*[int(myInput[1])] if len(myInput) >1 else [])

    print(sum(mySet))