import numpy

if __name__ == "__main__":
    myInput = str(input()).split()
    myArray1 = numpy.array([input().strip().split() for _ in range(int(myInput[0]))], int)
    myArray2 = numpy.array([input().strip().split() for _ in range(int(myInput[1]))], int)
    print(numpy.concatenate((myArray1, myArray2), axis = 0))