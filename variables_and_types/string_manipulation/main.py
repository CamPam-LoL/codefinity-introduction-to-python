grocery_items = "milk cheese bread apples oranges chicken" #grocery_items array

dairy1 = grocery_items[0:4] #First dairy item
dairy2 = grocery_items[5:11] #Second dairy item
bakery1 = grocery_items[12:17] #First bakery item
aisle_num = "aisle 5"

#message variable
message = f"We have dairy and bakery items: {dairy1}, {dairy2} , and {bakery1} in "

#print message function
print(message + aisle_num )