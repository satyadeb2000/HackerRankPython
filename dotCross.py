import numpy

if __name__ == "__main__":
    dim = int(input())
    arr1 = numpy.array([input().strip().split() for _ in range(int(dim))], int)
    arr2 = numpy.array([input().strip().split() for _ in range(int(dim))], int)
    print(numpy.dot(arr1, arr2))
    
