import pandas as pd # type: ignore

# Load dataset first (REQUIRED)
df = pd.read_csv(
    r"D:\AI ML ENGINEERING JOURNY\02_Python_Foundations\04_Pandas\dataset\students_performance.csv")  # Replace with your actual file name

# 1️⃣ Check for missing values (column-wise count)
print("Missing Values:\n", df.isnull().sum())

# 2️⃣ Fill missing values (example: replace NaN with 0)
# df['Hours_Spent'] = df['Hours_Spent'].fillna(0)

# OR fill with mean (better for numerical ML data)
# df['Hours_Spent'] = df['Hours_Spent'].fillna(df['Hours_Spent'].mean())

# 3️⃣ Remove duplicate rows
df = df.drop_duplicates()

# 4️⃣ Confirm changes
print("\nShape after cleaning:", df.shape)
