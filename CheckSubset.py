from __future__ import print_function
if __name__ == "__main__":
    for _ in range(int(input("Enter number of test cases:"))):
        numSetA = input("Enter number of elements of Set A: ")
        setA = set(map(int, input("Enter elements of set A: ").split()))
        numSetB = input("Enter number of elements of Set B: ")
        setB = set(map(int, input("Enter elements of set B: ").split()))
        print(*["True" if len(setA.difference(setB)) ==0 else "False"])
