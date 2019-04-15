from collections import OrderedDict
def merge_the_tools(string, k):
    myList = [string[i:i+k] for i in range(0, len(string), int(k))]
    for i in range(len(myList)):
        print("".join(OrderedDict.fromkeys(myList[i])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)