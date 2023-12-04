# This script function to calculate numerical values that performs
# addition, substraction, division and multiplication
# This function accepts user input ie the 2 numerical values
# and print out the result value

# Prompt user to choose the operation.
print("Please choose which operation to perform:\n")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice = int(input())

# Prompt the user to enter the 2 numerical values
print("Enter the first and second value to perform the operation")
value_1 = int(input())
value_2 = int(input())
result = 0
if choice == 1:
    result = value_1 + value_2   # perform the addition function 
elif choice == 2:
    result = value_1 - value_2 # perform the subtraction function
elif choice == 3:
    result = value_1 * value_2 # perform the multiplication function
else:
   result = value_1 / value_2 # perform the division function

print("The result is",result) # print out the output
