import streamlit as st
import pandas as pd

st.title('BMI Calculator')

# Input fields
height = st.number_input('Height (in cm)', min_value=0.0, step=0.1)
weight = st.number_input('Weight (in kg)', min_value=0.0, step=0.1)

# BMI calculation with error handling
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f'Your BMI is: {bmi:.2f}')
else:
    st.write("Please enter a valid height greater than 0.")

# BMI Categories
st.write('### BMI Categories:')
st.write('Underweight = <18.5')
st.write('Normal weight = 18.5–24.9')
st.write('Overweight = 25–29.9')
st.write('Obesity = BMI of 30 or greater')
