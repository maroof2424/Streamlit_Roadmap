import streamlit as st
import pandas as pd

st.title("📚 Student Marks Viewer")

data = {
    "Student": ["Areeba", "Bilal", "Maroof", "Sana"],
    "Math": [88, 72, 91, 85],
    "Science": [92, 78, 89, 95],
    "English": [85, 80, 87, 88]
}

df = pd.DataFrame(data)
st.dataframe(df)

# Show as table too
st.table(df)

# JSON summary
st.json({
    "Topper": "Maroof",
    "Average Score": 87.3,
    "Subjects": ["Math", "Science", "English"]
})
