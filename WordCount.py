from __future__ import print_function
from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    WordCount = int(input("Enter the number of words: "))
    Words = OrderedCounter()
    Words = OrderedCounter(input("Enter a word: ") for _ in range(WordCount))
    print(len(Words))
    print(*Words.values())

     
