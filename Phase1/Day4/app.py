import streamlit as st
import pandas as pd

st.title("📊 Streamlit Day 4: displaying data")

data = {
    "Name":["Maroof","Ali","Zain"],
    "Score":[95,85,75],
    "Passed":[True,True,False]
}

df = pd.DataFrame(data)

st.header("🔎 Interactive DataFrame")
st.dataframe(df, use_container_width=True)

# st.table
st.header("📋 Static Table")
st.table(df)

# st.json
st.header("🧾 JSON Display")
st.json({
    "student": "Maroof",
    "skills": ["Python", "Streamlit", "ML"],
    "score": 95
})