from __future__ import print_function
from collections import Counter

NumOfShoes = int(input("Enter the number of shoes in stock:"))

ShoeSizes = []
while(len(ShoeSizes) != NumOfShoes):
    ShoeSizes = list(str(input("Enter the shoe sizes seperated by spaces: ")).split(' '))
    while ShoeSizes.__contains__(' '):
        ShoeSizes.remove(' ')

Customers = int(input("Enter the number of Customers:"))

CustomerDemand = []
for customer in range(0, Customers):
    CustomerDemand.append(tuple(input("enter the size and price of shoe for customer " + str(customer) + ": ").split(' ')))
    customer = customer + 1

finalPrice = 0
Inventory = Counter(ShoeSizes)

for demand in CustomerDemand:
    if demand[0] in Inventory.keys():
        if(int(Inventory[demand[0]])>0):
            finalPrice = finalPrice + int(demand[1])
            Inventory[demand[0]] = str(int(Inventory[demand[0]]) -1)

print(finalPrice)


