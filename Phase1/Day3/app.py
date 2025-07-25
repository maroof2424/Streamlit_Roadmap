import streamlit as st

st.title("🎮 Streamlit Day 3: Interactive Widgets")

name = st.text_input("👤 Enter your name:")
if name:
    st.write(f"Hello, **{name}**! 👋")

age = st.slider("🎂 Select your age", 1, 100, 18)
st.write(f"Your age is: {age}")

gender = st.radio("🧑‍🤝‍🧑 Select your gender:", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")

marks = st.number_input("📈 Enter your marks", min_value=0, max_value=100)
st.write(f"Marks entered: {marks}")

if st.button("✅ Submit"):
    st.success(f"Submitted successfully for {name}!")
