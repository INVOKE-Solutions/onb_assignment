# import streamlit as st

# def calculator():
#     continue_calculator = 'y'

#     while continue_calculator.lower() == 'y':
#         st.title("Simple Calculator")

#         st.write("Please choose which operation to perform:")
#         st.write("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

#         choice = st.number_input("Enter the operation number:", min_value=1, max_value=4, step=1, key="choice")

#         while choice not in [1, 2, 3, 4]:
#             st.write("That was an invalid selection. Please try again.")
#             choice = st.number_input("Enter the operation number:", min_value=1, max_value=4, step=1,key="choice")

#         st.write("Awesome! You chose operation number -->", choice)

#         value_1 = st.number_input("Enter the first value:",key="value_1")
#         value_2 = st.number_input("Enter the second value:",key ="value_2")
#         result = 0

#         if choice == 1:
#             result = value_1 + value_2
#         elif choice == 2:
#             result = value_1 - value_2
#         elif choice == 3:
#             result = value_1 * value_2
#         elif choice == 4:
#             result = round((value_1 / value_2), 3)

#         st.write("The result is:", result)

# if __name__ == '__main__':
#     calculator()

import streamlit as st
import subprocess

def run_calculator():
    process = subprocess.Popen(["python", "calculator.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()

    st.write("Output:")
    st.write(output)

    if error:
        st.write("Error:")
        st.write(error)

def main():
    st.title("Streamlit Calculator")

    st.write("Welcome to the Streamlit Calculator app!")

    run_calculator()

if __name__ == "__main__":
    main()
