if __name__ == "__main__":
    numArray, space, numSets = str(input()).rpartition(" ")
    myArray = list(map(int, input().split()))
    happySet = set(map(int, input().split()))
    sadSet = set(map(int, input().split()))
    print(sum([(x in happySet) - (x in sadSet) for x in myArray]))
    
