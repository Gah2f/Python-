import copy
fruits = ['Apple', 'Organge', 'Mango', 'Banana', 'Do', 'Wow'] 
fruits[0] = 'Grapes' 
fruits.append('Pomegranate')
fruits.pop()
fruits.remove('Mango')
fruits.sort()
print(fruits)
if 'Lemon' in fruits:
   print('Yes, Lemon is present in the list')
else: 
   print('No, Lemon is not present in the list')
    
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)

Original_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
Original_list[0][1] = 100
copied_list = copy.copy(Original_list)

print(Original_list)
print(copied_list)
# The difference between copy.copy() and copy.deepcopy() is that 
# copy.copy() creates a shallow copy of the original list, which means that it creates a new 
# list object but does not create new objects for the elements within the list. Instead, it references the same objects as the original list.
# On the other hand, copy.deepcopy() creates a deep copy of the original list, which means that it creates a new list object and also creates
# new objects for all the elements within the list, recursively copying any nested objects as well.
# copy() copies only the outer list.
# deepcopy() copies everything inside as well. 

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_3 = list_1 + list_2
list_1.extend(list_2)
print(list_1)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(even_numbers) 
print(odd_numbers)  

# Tuples AKA  Immutable Lists
# Tuple use parenthesis () instead of square brackets []

# Why tuples instead of lists?
# Think of:
# List = a backpack → you can open it, remove stuff, add stuff
# Tuple = a locked suitcase → once closed, nothing can change, Your data stays safe and Protects important values from accidental changes