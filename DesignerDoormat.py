if __name__ == '__main__':
    dot = ".|."
    dash = "-"
   

    length, space, breadth = str(input()).rpartition(" ")

    #Top cone
    for row in range(int(int(length)/2)):
        numofDashes = int((int(breadth) - (2*row+1)*3)/2)
        print((dash*numofDashes) +(dot*(2*row+1))+ (dash*numofDashes))

    #Welcome
    numofDashes = int((int(breadth) - 7)/2)
    print(str(dash)*numofDashes + "WELCOME" + str(dash)*numofDashes)
    
    #bottom cone
    for row in reversed(range(int(int(length)/2))):
        numofDashes = int((int(breadth) - (2*row+1)*3)/2)
        print((dash*numofDashes) +(dot*(2*row+1))+ (dash*numofDashes))

    