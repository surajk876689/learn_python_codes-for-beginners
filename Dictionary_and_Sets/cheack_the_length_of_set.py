s = set() # printing the length of the set, which is 3. This demonstrates that even though 20 and 20.0 are considered equal in Python, they are treated as distinct elements in a set, and '20' is also a different element due to being a string.
s.add(20) # adding an integer value to the set
s.add(20.0) # adding a float value to the set
s.add('20') # adding a string value to the set
print(s)# printing the set to show that it contains three different types of values (integer, float, and string)
a=len(s)# calculating the length of the set, which is 3 because it contains three unique elements (20, 20.0, and '20')
print(a)# printing the length of the set, which is 3. This demonstrates that even though 20 and 20.0 are considered equal in Python, they are treated as distinct elements in a set, and '20' is also a different element due to being a string.