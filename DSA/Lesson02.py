my_set_1 = set()
my_set_1.add(1)
my_set_1.add(2)
print(my_set_1)
my_set_1.update([3, 4, 5]) 
print(my_set_1)
my_set_2 = set([4, 5, 6])
my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)
my_set_1.remove(2)
print(my_set_1)
my_set_1.discard(10)
print(my_set_1)
#Discard does not raise an error if the element is not found, while remove does.
# my_set_1.clear() 
# print(my_set_1) 

my_set_3.pop() 

#Valid oprators for sets
# Union: |, Intersection: &, Difference: -, Symmetric Difference: ^
# Invalid operators for sets: +, *, /, //, **, %, [:]

#Frozen sets are immutable sets, meaning they cannot be modified after creation. They are created using the frozenset() function.
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)
my_frozenset.add(6)  # This will raise an error since frozensets are immutable