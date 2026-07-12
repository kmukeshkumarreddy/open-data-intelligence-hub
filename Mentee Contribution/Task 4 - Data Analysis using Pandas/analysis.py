import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())

print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean())

print("\nTotal Customers:", len(df))
print("Most common Contract:", df["Contract"].mode()[0])
