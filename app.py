import streamlit as st
import pandas as pd
st.write('Substraction of Two Numbers')
st.header("Enter the Two Numbers")
number1 = st.number_input("Enter the 1st number")
number2 = st.number_input("Enter the 2st number")
sub = number1 - number2
st.write('Substraction of Two Number are :')
st.write(sub)
