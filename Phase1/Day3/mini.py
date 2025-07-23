import streamlit as st

st.title("📝 Bio Form")

name = st.text_input("Your Name")
age = st.slider("Your Age", 10, 60)
course = st.selectbox("Choose your Course", ["Python", "Django", "ML", "Data Science"])
submit = st.button("Submit")

if submit:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old and learning {course}. Keep it up! 🚀")
