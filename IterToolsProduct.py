from __future__ import print_function
from itertools import product

if __name__ == "__main__":
    print(*list(product(map(int, input().split()), map(int, input().split()))))