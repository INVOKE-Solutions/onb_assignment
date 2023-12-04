# This script function to calculate numerical values that performs
# addition, substraction, division and multiplication
# This function accepts user input ie the 2 numerical values
# and print out the result value

# Prompt user to choose the operation.
continue_calculator = 'y'

while(continue_calculator == 'y'):
    print("Please choose which operation to perform:\n")
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
    choice = int(input())
    
    # Prompt the user to enter the choiced operation
    # if wrong, it prompts to re-enter the correct operation number
    while choice not in [1,2,3,4]:
        print("That was invalid selection please try again.")
        choice = int(input())

    print("Awesome! You chose operation number -->", choice)

    # Prompt the user to enter the 2 numerical values
    print("\nEnter the first and second value to perform the operation:")
    value_1 = int(input("First value: "))
    value_2 = int(input("Second value: "))
    result = 0
    if choice == 1:
        result = value_1 + value_2   # perform the addition function 
    elif choice == 2:
        result = value_1 - value_2 # perform the subtraction function
    elif choice == 3:
        result = value_1 * value_2 # perform the multiplication function
    elif choice == 4:
        result = round((value_1 / value_2),3) # perform the division function

    print("The result is:",result) # print out the output

    # Prompt the user to if wanted to continue to perform the calculation
    continue_calculator = input("\nLet's do next calculation? (y/n): ")
    print("\n")
