import numpy

if __name__ == "__main__":
    myInput = tuple(map(int, input().split()))
    print(numpy.zeros(myInput, dtype = numpy.int))
    print(numpy.ones(myInput, dtype = numpy.int))