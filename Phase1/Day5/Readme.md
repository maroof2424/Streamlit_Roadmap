## 🎯 **Day 4 Goals:**

* ✅ Learn how to display data in different formats
* ✅ Practice with `st.dataframe`, `st.table`, and `st.json`

---

## 📌 Functions Overview

| Function         | Purpose                         | Editable?                   |
| ---------------- | ------------------------------- | --------------------------- |
| `st.dataframe()` | Interactive scrollable table    | ✅ Yes (sortable, resizable) |
| `st.table()`     | Static table view               | ❌ No                        |
| `st.json()`      | Pretty-prints JSON/dictionaries | ❌ No                        |

---

## 💻 Code Example (Save as `app.py`)

```python
import streamlit as st
import pandas as pd

st.title("📊 Streamlit Day 4: Displaying Data")

# Sample DataFrame
data = {
    "Name": ["Maroof", "Ali", "Zain", "Sara"],
    "Score": [95, 88, 76, 90],
    "Passed": [True, True, False, True]
}

df = pd.DataFrame(data)

# st.dataframe
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
```

---

## ▶️ Run It

```bash
streamlit run app.py
```

---

## 🧠 Tip

Use:

* `st.dataframe()` when working with **real data analysis**, dashboards, or large datasets.
* `st.table()` when you need a **clean static view** of small data.
* `st.json()` for **debugging APIs, configs, dictionaries**, or response data.

---

## 🧪 Challenge: Your Marks Viewer

Create a simple marks report:

```python
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
```

