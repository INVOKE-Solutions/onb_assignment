import streamlit as st

def calculate(choice, num_1: float, num_2:float):
    if choice == "Addition":
         result = num_1 + num_2
    elif choice == "Substraction":
        result = num_1 - num_2
    elif choice == "Multiplication":
        result = num_1 * num_2
    elif choice == "Division" and num_2!=0:
        result = num_1 / num_2
    else:
        st.warning("In Second number, please enter a non-zero number.")
        result="Not defined"

    return result