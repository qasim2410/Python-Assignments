import streamlit as st

json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "zip_code": "10001"
    },
}
st.json(json_data, expanded=True)