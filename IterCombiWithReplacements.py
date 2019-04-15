from __future__ import print_function
from itertools import combinations_with_replacement

if __name__ == "__main__":
    myString, space, k = str(input()).rpartition(" ")
    print(*(["".join(x) for x in list(combinations_with_replacement(sorted(list(myString)), int(k)))]), sep = '\n')
