 #change the values inside a list which is contained in set S
s={1,2,3,4,"suraj",[5,7,8]}
print(type(s))
print(s)
''' the above code will give an error because we cannot change the values inside a list which is contained in a set.
 This is because sets are mutable, but the elements inside a set must be immutable. Since lists are mutable, they cannot be added to a set.
   Therefore, we cannot change the values inside a list that is contained in a set.'''