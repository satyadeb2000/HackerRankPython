from __future__ import print_function
from collections import Counter

if __name__ == "__main__":
    Size = input("Enter size of group: ")
    RoomList = input("Enter Room list: ").split()
    RoomCounter = Counter(RoomList)
    print(*[room for room in RoomCounter.keys() if RoomCounter[room] ==1])

