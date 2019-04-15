from collections import OrderedDict

NumOfItems = int(input("Enter Number of Items: "))

ShoppingList = OrderedDict()

for _ in range(NumOfItems):
    Item, space, Price = str(input("Enter Item and Price: ")).rpartition(" ")
    ShoppingList[str(Item)] = int(Price) + ShoppingList[Item] if Item in ShoppingList else int(Price)

for Item in ShoppingList:
    print(Item + " " + str(ShoppingList[Item]))