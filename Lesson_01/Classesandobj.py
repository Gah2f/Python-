result = 0
while True: 
    print('Enter the number to add to the total, or "done" to finish:') 
    unser_input = input('>')
    if unser_input != 'done':
        unser_input = int(unser_input)
        result = result + unser_input
    else: 
        print('The total is:', result)
        break
