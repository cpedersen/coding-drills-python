
# Previous way:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# List comprehension way:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#newlist = [expression for item in iterable if condition == True]
#newlist = [x for x in fruits if "a" in x]
#newlist = [x for x in fruits if x != "apple"]
#newlist = [x for x in fruits]
#newlist = [x for x in range(10)]
newlist = [x.upper() for x in fruits]

print(newlist)