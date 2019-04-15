from __future__ import print_function
import numpy as np


if __name__ == "__main__":
    A,B = [np.array([input().split()],int) for _ in range(2)]
    print(np.inner(A,B)[0][0],np.outer(A,B),sep="\n")