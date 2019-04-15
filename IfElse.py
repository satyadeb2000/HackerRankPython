if __name__ == '__main__':
    n = int(input("Enter a Integer: "))
    if n%2 > 0:
        print("Wierd")
    else:
        if (n >= 2 and n<= 5):
            print("Not Wierd")
        elif(n >= 6 and n<= 20):
            print("Wierd")
        elif (n>20):
            print("Not Wierd")

