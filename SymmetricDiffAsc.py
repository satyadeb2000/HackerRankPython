from __future__ import print_function
if __name__ == "__main__":
    NumSetA = input()
    setA = set(map(int, input().split()))
    NumSetB = input()
    setB = set(map(int, input().split()))
    print('\n'.join([str(x) for x in sorted(setA.symmetric_difference(setB))]))
