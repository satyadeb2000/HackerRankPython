from __future__ import print_function
from itertools import combinations

if __name__ == "__main__":
    myString, space, k = str(input()).rpartition(" ")
    for i in range(1, int(k)+1):
        print(*(["".join(x) for x in list(combinations(sorted(list(myString)), int(i)))]), sep = '\n')
