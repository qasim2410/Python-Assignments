import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("## Simple Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    # Ensure there are columns before selecting
    if not df.empty:
        st.subheader("Filter Data")
        selected_column = st.selectbox("Select Column", df.columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select Value", unique_values)

        # Filter data based on user selection
        filtered_data = df[df[selected_column] == selected_value]
        st.write(filtered_data)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select X-axis", df.columns)
        y_column = st.selectbox("Select Y-axis", df.columns)

        if st.button("Generate Plot"):
            fig, ax = plt.subplots()
            ax.plot(filtered_data[x_column], filtered_data[y_column], marker="o", linestyle="-")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"{y_column} vs {x_column}")
            st.pyplot(fig)
else:
    st.write("Waiting on file upload...")
