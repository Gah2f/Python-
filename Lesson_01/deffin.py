def nebiyu(): 
    print("Hello, Nebiyu!")

nebiyu()

def adder(a,b):
    print("The sum of", a, "and", b, "is", a + b)
adder(5, 10)

def adder(a,b):
    return a + b
adder(5, 10) 

print(adder(5, 10))

def summer(a, b):
    if (type(a) != int) or (type(b) != int):
        return 
    return a + b
total = summer("5", 10) 
# It will return None because "5" is not an integer, take care 
# the first return statement is executed  
print(total)
