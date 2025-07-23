
## 🎯 **Day 3 Goals:**

* ✅ Learn the most used **input functions** in Streamlit
* ✅ Capture user input and display dynamic responses

---

## 📌 Input Widgets You’ll Learn

| Function            | Purpose                            |
| ------------------- | ---------------------------------- |
| `st.button()`       | Executes code on button click      |
| `st.text_input()`   | Takes text from user               |
| `st.number_input()` | Takes a numeric value              |
| `st.slider()`       | Allows user to choose from a range |
| `st.radio()`        | Select one option from a list      |
| `st.selectbox()`    | Dropdown to select one item        |

---

## 💻 Example App (Save as `app.py`)

```python
import streamlit as st

st.title("🎮 Streamlit Day 3: Interactive Widgets")

# Text Input
name = st.text_input("👤 Enter your name:")
if name:
    st.write(f"Hello, **{name}**! 👋")

# Slider
age = st.slider("🎂 Select your age", 1, 100, 18)
st.write(f"Your age is: {age}")

# Radio Buttons
gender = st.radio("🧑‍🤝‍🧑 Select your gender:", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")

# Number Input
marks = st.number_input("📈 Enter your marks", min_value=0, max_value=100)
st.write(f"Marks entered: {marks}")

# Button
if st.button("✅ Submit"):
    st.success(f"Submitted successfully for {name}!")
```

---

## ▶️ Run It

```bash
streamlit run app.py
```

Then try:

* Typing your name
* Moving the slider
* Choosing options
* Clicking the button

---

## 🎒 Homework Challenge

Create a **Mini Bio App** using these widgets:

```python
st.title("📝 Bio Form")

name = st.text_input("Your Name")
age = st.slider("Your Age", 10, 60)
course = st.selectbox("Choose your Course", ["Python", "Django", "ML", "Data Science"])
submit = st.button("Submit")

if submit:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old and learning {course}. Keep it up! 🚀")
```

---
Perfect! Welcome to **Day 3**, Maroof!
Today, we’ll make your Streamlit app **interactive** using input widgets like buttons, sliders, text boxes, and more.

---

## 🎯 **Day 3 Goals:**

* ✅ Learn the most used **input functions** in Streamlit
* ✅ Capture user input and display dynamic responses

---

## 📌 Input Widgets You’ll Learn

| Function            | Purpose                            |
| ------------------- | ---------------------------------- |
| `st.button()`       | Executes code on button click      |
| `st.text_input()`   | Takes text from user               |
| `st.number_input()` | Takes a numeric value              |
| `st.slider()`       | Allows user to choose from a range |
| `st.radio()`        | Select one option from a list      |
| `st.selectbox()`    | Dropdown to select one item        |

---

## 💻 Example App (Save as `app.py`)

```python
import streamlit as st

st.title("🎮 Streamlit Day 3: Interactive Widgets")

# Text Input
name = st.text_input("👤 Enter your name:")
if name:
    st.write(f"Hello, **{name}**! 👋")

# Slider
age = st.slider("🎂 Select your age", 1, 100, 18)
st.write(f"Your age is: {age}")

# Radio Buttons
gender = st.radio("🧑‍🤝‍🧑 Select your gender:", ["Male", "Female", "Other"])
st.write(f"You selected: {gender}")

# Number Input
marks = st.number_input("📈 Enter your marks", min_value=0, max_value=100)
st.write(f"Marks entered: {marks}")

# Button
if st.button("✅ Submit"):
    st.success(f"Submitted successfully for {name}!")
```

---

## ▶️ Run It

```bash
streamlit run app.py
```

Then try:

* Typing your name
* Moving the slider
* Choosing options
* Clicking the button

---

## 🎒 Homework Challenge

Create a **Mini Bio App** using these widgets:

```python
st.title("📝 Bio Form")

name = st.text_input("Your Name")
age = st.slider("Your Age", 10, 60)
course = st.selectbox("Choose your Course", ["Python", "Django", "ML", "Data Science"])
submit = st.button("Submit")

if submit:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old and learning {course}. Keep it up! 🚀")
```

---
