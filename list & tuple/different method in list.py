list=[1,22,33,99,54,67,346,6,4,6,6,45,4,45,45,4,6,45,6,4435,423,5,34,566,46,6,6,343546445,4455445,]
#different method in list
#1. append() method is used to add an element to the end of the list.
list.append(100)
print("append",list) # Output: [1, 22, 33, 99, 54, 67, 346, 6, 4, 6, 6, 45, 4, 45, 45, 4, 6, 45, 6, 4435, 423, 5, 34, 566, 46, 6, 6, 343546445, 4455445, 100]
#2. remove() method is used to remove the first occurrence of a specified value from the
list.remove(33)
print("remove",list)
# Output: [1, 22, 99, 54, 67, 346, 6, 4, 6, 6, 45, 4, 45, 45, 4, 6, 45, 6, 4435, 423, 5, 34, 566, 46, 6, 6, 343546445, 4455445, 100]
#3. insert() method is used to insert an element at a specific index in the list. The first argument is the index where the element should be inserted, and the second argument is the value to be inserted.
list.insert(2, 50)
print("insert",list)    
# Output: [1, 22, 50, 99, 54, 67, 346, 6, 4, 6, 6, 45, 4, 45, 45, 4, 6, 45, 6, 4435, 423, 5, 34, 566, 46, 6, 6, 343546445, 4455445, 100]
#4. pop() method is used to remove and return the last element from the list. If you want to remove an element at a specific index, you can pass the index as an argument to the pop() method.
list.pop()          
print("pop",list)
# Output: [1, 22, 50, 99, 54, 67, 346, 6, 4, 6, 6, 45, 4, 45, 45, 4, 6, 45, 6, 4435, 423, 5, 34, 566, 46, 6, 6, 343546445, 4455445]
#5. clear() method is used to remove all elements from the list, leaving it empty
list.clear()
print("clear",list) # Output: []
#6. sort() method is used to sort the elements of the list in ascending order. You can also use the reverse=True argument to sort the list in descending order.
list=[1,22,33,99,54,67,346,6,4,6,6,45,4,45,45,4,6,45,6,4435,423,5,34,566,46,6,6,343546445,4455445]
list.sort()
print("sort",list) # Output: [1, 4, 4, 4, 5, 6, 6, 6, 6, 22, 33, 45, 45, 45, 46, 54, 67, 99, 346, 423, 566, 4435, 343546445, 4455445]
#reverse() method is used to reverse the order of the elements in the list.
list.reverse()  
print("reverse",list) # Output: [4455445, 343546445, 4435, 566, 423, 346, 99, 67, 54, 46, 45, 45, 45, 33, 22, 6, 6, 6, 6, 5, 4, 4, 4, 1]
