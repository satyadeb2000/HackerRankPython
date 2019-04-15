import numpy
if __name__ == "__main__":
   myArray = numpy.array(list(map(int, input().split())))
   myArray.shape = (3,3)
   print(myArray)

   