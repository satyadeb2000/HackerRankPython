from __future__ import print_function
if __name__ == "__main__":
    setA = set(map(int, input("Enter elements of set A: ").split()))
    result = True
    for _ in range(int(input("Enter number of test cases:"))):
        setB = set(map(int, input("Enter elements of set B: ").split()))
        result = result and ( True if (setB.issubset(setA) and (len(setA) > len(setB))) else False)

    print(result)