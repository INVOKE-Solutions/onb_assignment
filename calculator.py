# This script function to calculate numerical values that performs
# addition, substraction, division and multiplication

# Please choose which operation to perform:
print("Please choose which operation to perform:\n")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice = int(input())

print("Enter the first and second value to perform the operation")
value_1 = int(input())
value_2 = int(input())
result = 0
if choice == 1:
    result = value_1 + value_2   
elif choice == 2:
    result = value_1 - value_2
elif choice == 3:
    result = value_1 * value_2
else:
   result = value_1 / value_2
   
print("The result is",result)
