if __name__ == '__main__':
    s = input()
    #print(any(str(x).isalnum() for x in s ))
    #print(any(str(x).isalpha() for x in s ))
    #print(any(str(x).isdigit() for x in s ))
    #print(any(str(x).islower() for x in s ))
    #print(any(str(x).isupper() for x in s ))
    
    for cmd in ["isalnum", "isalpha", "isdigit", "islower", "isupper"]:
        print(any(eval("c." + cmd + "()") for c in s))
    