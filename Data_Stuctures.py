#Append Example
print("Append Example")
list1 = ["Hello","Beautiful","World"]
list2 = [6,7,8,9,10]
list1.append(list2)
print(list1)
print("____________________________________________")

#Extend Example
print("Extend Example")
list3 = ["Hello","Beautiful","World"]
list4 = [6,7,8,9,10]
list3.extend(list4)
print(list3)
print("____________________________________________")

#Insert Example
print("Insert Example")
fruits1 = ["apple","orange","watermelon",'pear', 'banana', 'kiwi']
fruits1.insert(1,"strawberries")
print(fruits1)
print("____________________________________________")

#Remove Example
print("Remove Example")
fruits2 = ["apple","orange","watermelon",'pear', 'banana', 'kiwi']
fruits2.remove("orange")
print(fruits2)
print("____________________________________________")

#Pop Example
print("Pop Example")
print(fruits2.pop(0))
print("____________________________________________")

#Count/Index
print("Count and Index Example")
vehicles = ["car","bus","train","plane","car","train"]
print("The count of cars: "+ str(vehicles.count("car")))
print("the index of train: "+ str(vehicles.index("train")))
print("the index of next train starting a position 3: "+ str(vehicles.index("train",3)))
print("____________________________________________")

#Reverse/Sort
print("Sort and Reverse Example")
vehicles = ["car","bus","train","plane","car","train"]
vehicles.reverse()
print(vehicles)
vehicles.sort()
print(vehicles)
print("____________________________________________")