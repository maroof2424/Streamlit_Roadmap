Great, Maroof! Let’s start **Day 1** of your **Streamlit roadmap**.

---

## 🎯 **Day 1 Goal:**

✅ Understand what Streamlit is
✅ Set up your environment
✅ Run your first Streamlit app

---

## 📌 Step 1: What is Streamlit?

> **Streamlit** is a Python framework to quickly build and share beautiful **data apps** and **ML dashboards** — all in Python, no HTML/CSS/JS needed.

Think of it like turning your Python scripts into interactive web apps **with just a few lines of code**.

---

## 📦 Step 2: Install Streamlit

### ✅ If using terminal or command prompt:

```bash
pip install streamlit
```

### ✅ (Optional but recommended) Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  ## On Linux/macOS
pip install streamlit
```

---

## 👨‍💻 Step 3: Your First Streamlit App

### 👉 Create a file named `app.py` and write:

```python
import streamlit as st

st.title("👋 Hello, Maroof!")
st.header("Welcome to Day 1 of Streamlit")
st.write("Streamlit makes it super easy to create web apps with Python.")
```

---

## ▶️ Step 4: Run the App

Open terminal in the folder where `app.py` is located and run:

```bash
streamlit run app.py
```

This will open your app in the browser at `http://localhost:8501`.

---

## 💡 Bonus Tips

* To **stop** the app, press `Ctrl+C` in the terminal.
* You can **edit the file** and the browser will auto-refresh (Hot Reload).
* All Streamlit apps must start with `import streamlit as st`.

---

## ✅ Homework / Practice

1. Add more elements to your `app.py`:

```python
st.text("This is simple text.")
st.markdown("### This is a markdown heading")
st.code("print('This is code')")
```

2. Explore:

   * [✅] What is `st.title()`
   * [✅] What is `st.write()`
   * [✅] What is the difference between `st.text()` and `st.markdown()`

