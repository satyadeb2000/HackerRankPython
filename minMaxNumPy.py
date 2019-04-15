import numpy 


if __name__ == "__main__":
    Row, space, Col = str(input()).rpartition(" ")
    myArray = numpy.array([input().strip().split() for _ in range(int(Row))], int)
    print(numpy.max(numpy.min(myArray, axis = 1)))