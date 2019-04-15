import numpy 


if __name__ == "__main__":
    Row, space, Col = str(input()).rpartition(" ")
    myArray = numpy.array([input().strip().split() for _ in range(int(Row))], int)
    numpy.set_printoptions(legacy='1.13')
    print(numpy.mean(myArray, axis = 1))
    print(numpy.var(myArray, axis = 0))
    print(numpy.std(myArray))