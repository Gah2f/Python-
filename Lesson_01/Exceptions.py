
x = 1
try :
    print(x) 
except NameError:
    print("There is no 'x' ")

try: 
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by 0")
finally:
    print("Just passed, I am printing everything! very tired!")