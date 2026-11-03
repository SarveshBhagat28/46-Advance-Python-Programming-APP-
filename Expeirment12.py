import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Age": [24, 27, 22, 32, 29, 25, 100],
    "MonthlyCharge": [500, 600, 520, 580, 620, 550, 6000],
    "Tenure": [2, 12, 8, 24, 18, 6, 1],
    "Churn": ["Yes", "No", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)
df.loc[2, "Age"] = None
df.loc[3, "MonthlyCharge"] = None

print("Dataset:\n", df)
print("\nDescriptive statistics:\n", df.describe())

print("Mean age:", df["Age"].mean())
print("Median age:", df["Age"].median())
print("Mode age:", df["Age"].mode()[0])
print("Standard deviation:", df["Age"].std())
print("Variance:", df["Age"].var())
print("Minimum age:", df["Age"].min())
print("Maximum age:", df["Age"].max())
print("Quantiles:\n", df["Age"].quantile([0.25, 0.5, 0.75]))

print("\nMissing values:\n", df.isnull().sum())

df_dropped = df.dropna()
print("\nRows after dropping missing values:\n", df_dropped)

df_filled = df.copy()

for column in ["Age", "MonthlyCharge", "Tenure"]:
    df_filled[column] = df_filled[column].fillna(df_filled[column].mean())

print("\nAfter filling missing values:\n", df_filled)

lower_age = df_filled["Age"].mean() - 3 * df_filled["Age"].std()
upper_age = df_filled["Age"].mean() + 3 * df_filled["Age"].std()

lower_charge = df_filled["MonthlyCharge"].mean() - 3 * df_filled["MonthlyCharge"].std()
upper_charge = df_filled["MonthlyCharge"].mean() + 3 * df_filled["MonthlyCharge"].std()

df_no_outliers = df_filled[
    (df_filled["Age"].between(lower_age, upper_age)) &
    (df_filled["MonthlyCharge"].between(lower_charge, upper_charge))
]

print("\nData after removing outliers:\n", df_no_outliers)

df_filled["Age_capped"] = df_filled["Age"].clip(lower=lower_age, upper=upper_age)
df_filled["Charge_capped"] = df_filled["MonthlyCharge"].clip(
    lower=lower_charge, upper=upper_charge
)

plt.hist(df_filled["Age"], bins=5, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(y=df_filled["Age"])
plt.title("Box Plot of Age")
plt.show()

plt.scatter(df_filled["Age"], df_filled["MonthlyCharge"])
plt.title("Age vs Monthly Charge")
plt.xlabel("Age")
plt.ylabel("Monthly Charge")
plt.show()

numeric_df = df_filled[["Age", "MonthlyCharge", "Tenure"]]

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
