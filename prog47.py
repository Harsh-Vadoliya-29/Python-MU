import pandas as pd
import numpy as np

data = {
    "Name": ["Aarav", "Priya", None, "Sneha", "Vikram"],
    "Age": [25, np.nan, 35, 28, np.nan],
    "Salary": [50000, 60000, np.nan, np.nan, 45000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nMissing values:\n", df.isnull().sum())

df_dropped = df.dropna()
print("\nAfter dropna():")
print(df_dropped)

df_filled = df.fillna({"Name": "Unknown", "Age": df["Age"].mean(), "Salary": 0})
print("\nAfter fillna():")
print(df_filled)
