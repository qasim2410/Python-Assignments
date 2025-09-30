import streamlit as st

name = st.text_input("Enter your name:")
age = st.text_input("Enter your age:")
favorite_number = st.text_input("Enter your favorite number:")

if st.button("Submit"):
    st.write(f"Your name: {name}")
    st.write(f"Your age: {age}")
    st.write(f"Your favorite number: {favorite_number}")