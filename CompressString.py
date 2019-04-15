from __future__ import print_function
from itertools import groupby

if __name__ == "__main__":
    print(*[(len(list(g)), int(k)) for k, g in groupby(input())])