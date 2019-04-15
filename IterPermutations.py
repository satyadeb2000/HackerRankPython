from __future__ import print_function
from itertools import permutations

if __name__ == "__main__":
    myString, space, k = str(input()).rpartition(" ")
    print(*sorted(["".join(x) for x in list(permutations(list(myString), int(k)))]), sep = '\n')
