if __name__ == "__main__":
    NumA = input("Enter number of elements of set A: ")
    SetA = set(input("Enter elements of Set A: ").split())

    for _ in range(int(input("Enter number of other sets: "))):
        command, space, NumB = str(input("Enter operation, num of elements of set B: ")).rpartition(" ")
        SetB = set(input("Enter elements of Set B: ").split())
        getattr(SetA, command)(SetB)

    print(sum(map(int, SetA)))