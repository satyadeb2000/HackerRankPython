import numpy

if __name__ == "__main__":
    dim = int(input())
    arr1 = numpy.array([input().strip().split() for _ in range(int(dim))], float)
    print(round(numpy.linalg.det(arr1), 2))