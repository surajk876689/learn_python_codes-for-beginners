#list is a mutable data type, which means that you can change the contents of a list after it has been created. You can add, remove, or modify elements in a list.
#Example of modifying a list
my_list = [1, 2, 3, 4, 5]
print(my_list) # Output: [1, 2, 3, 4, 5]
my_list[0] = 10 # Modifying the first element of the list
print("0=10",my_list) # Output: [10, 2, 3, 4, 5]
my_list.append(6) # Adding a new element to the end of the list
print("appentd",my_list) # Output: [10, 2, 3, 4,
[5, 6]
my_list.remove(2) # Removing an element from the list
print("remove",my_list) # Output: [10, 3, 4, 5, 6]
my_list.insert(1, 20) # Inserting an element at a specific index
print("insert",my_list) # Output: [10, 20, 3, 4, 5, 6]
my_list.pop() # Removing the last element from the list
print("pop",my_list) # Output: [10, 20, 3, 4,
[5]
my_list.clear() # Removing all elements from the list
print("clear",my_list) # Output: []
