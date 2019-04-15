
if __name__ == "__main__":
    Count = input()
    integer_list = map(int, input().split())
    myTupple = tuple(integer_list)
    print(hash(myTupple))