"""
    Streamlit Simple Calculator.

    Author: Putri Khalilah Kamaluddin
    Date: 2023/12/05
    Description: This file is used to launch a minimal streamlit web 
	application. A simple calculator that calculates 2 numerical values with addition,
    substraction, multiplication and division operator.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/
"""

#Streamlit depends 
import streamlit as st #  pip install streamlit
from calculator import addition, multiplication,division,substraction

def main():

    st.title("Simple Calculator")
    st.write("Please choose which operation to perform:")
    st.write("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    choice = st.number_input("Enter the operation number:", min_value=1, max_value=4, step=1)

    # to remove the "+/-" signs in the entering number widgets
    st.markdown("""
    <style>
        button.step-up {display: none;}
        button.step-down {display: none;}
        div[data-baseweb] {border-radius: 4px;}
    </style>""",
    unsafe_allow_html=True)

    value_1 = st.number_input("Enter the first value:",key="value_1", placeholder='Type a number...')
    value_2 = st.number_input("Enter the second value:",key ="value_2", placeholder='Type a number...')
    result = 0

    if choice == 1:
        result = addition(value_1,value_2)
    elif choice == 2:
        result= substraction(value_1,value_2)
    elif choice == 3:
        result = multiplication(value_1,value_2)
    elif choice == 4:
        result = division(value_1,value_2)

    st.write("The result is:", result)

if __name__=='__main__':
    main()







