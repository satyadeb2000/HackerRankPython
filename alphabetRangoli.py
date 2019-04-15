def print_rangoli(size):
    rangoli = ""
    breadth = (4*size-3)

    for line in range(int(size)):
        alphaBreadth = (4*line + 1)
        dashwidth = int(((breadth - alphaBreadth))/2)
        alphastring = "-".join([chr(96 + size - x) for x in range(int(line+1))] + [chr(96 + size - line + x) for x in range(1, int(line + 1))])
        
        rangoli = rangoli + ("-"*dashwidth) + alphastring + ("-"*dashwidth) + "\n"

    for line in reversed(range(int(size - 1))):
        alphaBreadth = (4*line + 1)
        dashwidth = int(((breadth - alphaBreadth))/2)
        alphastring = "-".join([chr(96 + size - x) for x in range(int(line+1))] + [chr(96 + size - line + x) for x in range(1, int(line + 1))])
        rangoli = rangoli + ("-"*dashwidth) + alphastring + ("-"*dashwidth) + "\n"

    print(rangoli)
        
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)