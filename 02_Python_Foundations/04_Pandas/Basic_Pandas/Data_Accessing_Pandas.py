import pandas as pd

data = {
    "Name": ["Partha", "Pritam", "Argha"],
    "Age": [21, 15, 16],
    "Marks": [90, 99, 80]
}
df = pd.DataFrame(data)
print(df)

print("----For Access Columns----")
print(df["Name"])
print("----------------------------------")
print(df[["Name", "Marks"]])
print("---------------------------------")
print(df[["Name", "Age", "Marks"]])

print("------------------------------------")

print("_____________Access Rows_____________")
print("Using iloc (index based)")
print(df.iloc[0])
print("df.iloc[0] print the 1st row ")

print(df.iloc[0:2])
print("df.iloc[0:2] print the 1st two  row ")
print("________________________________")
print("Using loc (label based)")
print(df.loc[0])
print()
print(df.loc[1])

"""
## 🎯 When to Use `df.iloc` vs `df.loc` — **Practical Rules**

No theory. These are **decision rules** you should apply instantly while coding. ⚙️📊

---

## ✅ Use `df.iloc` **WHEN** (Position Matters)

### 1️⃣ You care about **row number**, not label

```python
df.iloc[0]        # first row
df.iloc[-1]       # last row
```

📌 Typical in **loops, batches, model training**

---

### 2️⃣ You are slicing like Python / NumPy

```python
X = df.iloc[:, :-1]   # all rows, all columns except last
y = df.iloc[:, -1]   # target column
```

📌 **Very common in ML pipelines**

---

### 3️⃣ Index is messy / unknown / auto-generated

```python
df.iloc[10:20]
```

📌 Safer when index labels are unreliable

---

### 4️⃣ Performance-critical operations

* `iloc` is **slightly faster**
* Used in **internal algorithms**

---

## ✅ Use `df.loc` **WHEN** (Meaning Matters)

### 1️⃣ You know **column names**

```python
df.loc[:, "Marks"]
df.loc[:, ["Name", "age"]]
```

📌 Best for **readable, maintainable code**

---

### 2️⃣ Filtering with conditions (MOST IMPORTANT)

```python
df.loc[df["Marks"] > 90]
```

📌 Industry-standard for **data analysis**

---

### 3️⃣ Index has semantic meaning

```python
df.loc[0:2]
```

📌 Includes end label → predictable for humans

---

### 4️⃣ Updating values safely

```python
df.loc[df["age"] < 18, "Marks"] = 0
```

📌 Prevents `SettingWithCopyWarning`

---

## 🔥 Real-World Usage Pattern (THIS IS HOW PROS DO IT)

| Task                    | Use    |
| ----------------------- | ------ |
| Train/Test split        | `iloc` |
| Feature/target split    | `iloc` |
| Filtering rows          | `loc`  |
| Selecting named columns | `loc`  |
| Updating data           | `loc`  |
| Quick positional check  | `iloc` |

---

## 🧠 One-Line Mental Model

> **If you think in numbers → `iloc`
> If you think in names/conditions → `loc`**

---

## 🚨 Interview-Safe Answer

> *I use `iloc` for positional slicing in ML workflows and 
`loc` for label-based selection and conditional filtering in data analysis.*

"""
