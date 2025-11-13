num1 = input('Enter first number')
num2 = input('Enter second number') 
op = input('Enter operator (+, -, *, /): ') 

if op == '+': 
    result = float(num1) + float(num2)
    print(result)
elif op == '-':
    result = float(num1) - float(num2) 
    print(result)
elif op == '*':
    result = float(num1) * float(num2)
    print(result)
elif op == '/':
    result = float(num1) / float(num2)
    print(result)
else: 
    result = 'Invalid operator'
    print(result)