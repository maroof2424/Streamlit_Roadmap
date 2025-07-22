## 🎯 **Day 2 Goals:**

* ✅ Understand the difference between `st.title()`, `st.header()`, `st.write()`, and `st.text()`
* ✅ Practice using them in a Streamlit app

---

## 🧠 Concepts Explained

| Function      | Description                                                       | Example                                  |
| ------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| `st.title()`  | Creates a big main title                                          | `st.title("🚀 Welcome to Streamlit")`    |
| `st.header()` | Section heading (smaller than title)                              | `st.header("Section 1: Overview")`       |
| `st.text()`   | Displays plain text                                               | `st.text("This is plain text.")`         |
| `st.write()`  | The most flexible one – can write text, numbers, dataframes, etc. | `st.write("This can display anything!")` |

---

## 💻 Code Example (Save as `app.py`)

```python
import streamlit as st

# Title
st.title("🎯 Streamlit Day 2: Basic Display Elements")

# Header
st.header("📘 Heading Section")

# Text
st.text("This is plain text. Good for small notes.")

# Write (Flexible)
st.write("✅ `st.write()` can show strings, numbers, lists, and even DataFrames!")

# Bonus examples
st.write(42)
st.write(["Python", "Streamlit", "Data Science"])
st.write({"name": "Maroof", "skill": "Streamlit"})
```

---

## ▶️ Run It

```bash
streamlit run app.py
```

You’ll see:

* A big title
* A section header
* Plain text
* A list and dictionary rendered automatically

---

## 🧠 Summary / Tip of the Day

* Use `st.title()` once at the top.
* Use `st.header()` to separate sections.
* Use `st.text()` for plain info, like log messages.
* Use `st.write()` **almost everywhere** — it’s your best friend in Streamlit.

---

## ✅ Mini Challenge

Make your own info dashboard:

```python
st.title("📊 My Personal Dashboard")

st.header("👨‍💻 About Me")
st.text("Name: Maroof\nLearning: Python, Streamlit\nInstitute: MITI")

st.header("📌 Goals")
st.write([
    "✔️ Master Streamlit",
    "✔️ Build ML Projects",
    "✔️ Deploy on Streamlit Cloud"
])
```

