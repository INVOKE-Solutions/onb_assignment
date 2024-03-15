"""
# Calculator Interface
"""

import streamlit as st
from calculator import calculate
st.title("Simple Calculator")
st.write("1. Insert 2 values you want to calculate in ")
num_1 = st.number_input("First Number:",key='num_1')
num_2 = st.number_input("Second Number:",key='num_2')
result=0

st.write("2. Then, ")
choice=st.selectbox("select any of the operation below:",["Addition","Substraction","Multiplication","Division"])

if st.button("Calculate"):
    result = calculate(choice, num_1, num_2)
    st.success(f"Answer = {result}")