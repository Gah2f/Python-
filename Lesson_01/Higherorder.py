from functools import reduce

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def operate(func,x,y):
    return func(x,y)

print(operate(add, 5, 3))
print(operate(sub, 5, 3)) 


numbers = [2,3,4,6,2] 
squared_numbers = map(lambda num: num * num, numbers)
print(list(squared_numbers)) 

numbers = [23,34,2,3,2]

sqrrootnumbers = map(lambda num : num ** 0.5, numbers)
print(list(sqrrootnumbers)) 

filtered_numbers = filter(lambda num : num % 2 == 0, numbers)
print(list(filtered_numbers)) 

name = ["John", "Jane", "Doe", "Alice", "Bob"]

char_count = reduce(lambda x, y: x + len(y), name, 0)
print(char_count)