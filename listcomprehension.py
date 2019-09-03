# This will teach you about the list comprehension in python


items = [2,4,3,67,89,45,7, 6, 8,51,98,45,65,709, -56]
# Let's create the copy of the items to the cashier
cashier = [item for item in items]
print(cashier)
#Lets filter out the times greater than 50
cashier=[item for item in items if item>50]
print(cashier)
# Add 100 to each item if item is even and greater than 5
cashier=[item +100 for item in items if item%2==0 and item > 5]
print(cashier)