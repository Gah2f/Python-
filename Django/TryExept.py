try:
   num = int(input("Enter a number: ")) 
   
   print("You entered:", num) 
 
except ValueError:
    print("Invalid input. Please enter a valid number.")
else: 
    print("Thank you for entering a valid number.")
finally: 
    print("Execution completed.")