import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["A", "B", "C"]
)
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
st.dataframe(data)
st.table(data)
st.json({"name": "Qasim", "age": 25, "city": "Karachi"})
st.metric(label="Temperature", value="20 °C", delta="1 °C")
st.code("import streamlit as st", language="python")
st.image("https://via.placeholder.com/150", caption="Sample Image")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# st.map(data)
# st.title("My Streamlit App")


# Collect user input
# name = st.text_input("Enter your name:")
# age = st.slider("Enter your age:")
# favorite_number = st.text_input("Enter your favorite number:")

# # Display the inputs
# st.write(f"Your name: {name}")
# st.write(f"Your age: {age}")
# st.write(f"Your favorite number: {favorite_number}")

# if st.button("Submit"):
#     st.write("Button clicked!")

# age = st.slider("Select your age", 0, 100, 25)
# st.write("Your age is:", age)

# checked = st.checkbox("Check me!")
# if checked:
#     st.write("Checkbox is checked!")

# if st.button("Click Me"):
#    st.write("Button Clicked")

    


# name = "Qasim Hussain"

# number = 10
# st.write("Hello, Streamlit!", name)
# st.write("The random number is:", number)
# st.title("Streamlit Fundamentals")

# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a simple text output")
# st.markdown("This is a **hello python** text output")

# st.text_input("Enter some text:")

# st.button("Submit")