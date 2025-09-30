import streamlit as st

age = st.number_input("Select your age", 0, 100, 25)

st.write("Your age is:", age)