# calculator_app.py
from calculator import add,subtract,multiply,divide
import streamlit as st

def calculator():
    st.title("Simple Calculator")

    # Get user input
    num1 = st.number_input("Enter the first number:")
    operation = st.selectbox("Select operation:", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter the second number:")

    # Perform calculation
    result = 0
    if operation == "+":
        result = add(num1,num2)
    elif operation == "-":
        result = subtract(num1,num2)
    elif operation == "*":
        result = multiply(num1,num2)
    elif operation == "/":
        if num2 != 0:  # Check for division by zero
            result = divide(num1,num2)
        else:
            st.error("Error: Division by zero")

    # Display result
    st.write("Result:", result)

if __name__ == "__main__":
    calculator()