from __future__ import print_function
from collections import defaultdict

myInput = list(str(input()).split(' '))
Original = defaultdict(list)

for counter in range(1, int(myInput[0]) + 1):
    Original[str(input("Enter members of A:"))].append(str(counter))

verify = []
for counter in range(1, int(myInput[1]) + 1):
    verify.append(input("Enter members of B:"))

for item in verify:
    if len(Original[item]):
        print(' '.join(Original[item]))
    else:
        print("-1")