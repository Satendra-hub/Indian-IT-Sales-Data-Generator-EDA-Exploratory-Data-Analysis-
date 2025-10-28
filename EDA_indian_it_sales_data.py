# 📦 Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🎨 Step 2: Set Plot Theme (Modern Seaborn Style)
sns.set_theme(style="whitegrid")

def add(a, b):
    return np.add(a, b)
pass

# 📁 Step 3: Load CSV and Convert to DataFrame
# CSV file must be in the same folder or provide full path
df = pd.read_csv("indian_it_sales_data.csv")  # ✅ CSV को DataFrame में बदलना

# 📌 Step 4: Basic Structure of Data
print("✅ Dataset Shape (rows, columns):", df.shape)
print("✅ Column Names:", df.columns.tolist())
print("✅ First 5 Rows:\n", df.head())

# 🧠 Step 5: Data Types and Null Values
print("\n🔍 Data Types:\n", df.dtypes)
print("\n❓ Missing Values:\n", df.isnull().sum())

# 📊 Step 6: Summary Statistics for Numerical Columns
print("\n📊 Summary Statistics:\n", df.describe())

# 🔢 Step 7: Unique Values in Each Column
print("\n🔢 Unique Values per Column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# 📈 Step 8: Distribution of Monthly Revenue
plt.figure(figsize=(8, 4))
sns.histplot(df['monthly_revenue'], kde=True, color='skyblue')
plt.title("Distribution of Monthly Revenue (₹ lakhs)")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# 📊 Step 9: Company-wise Project Count
plt.figure(figsize=(8, 4))
sns.countplot(x='company_name', data=df, palette='Set2')
plt.title("Projects by Company")
plt.xlabel("Company")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 📍 Step 10: Region-wise Average Revenue
region_revenue = df.groupby('region')['monthly_revenue'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 4))
region_revenue.plot(kind='bar', color='coral')
plt.title("Average Monthly Revenue by Region")
plt.ylabel("Revenue (₹ lakhs)")
plt.xlabel("Region")
plt.show()

# 📅 Step 11: Project Duration Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['project_duration'], bins=10, kde=True, color='green')
plt.title("Distribution of Project Duration (months)")
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.show()

# ⭐ Step 12: Client Rating Distribution
plt.figure(figsize=(8, 4))
sns.countplot(x='client_rating', data=df, palette='coolwarm')
plt.title("Client Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# 🔗 Step 13: Correlation Matrix (Numerical Features)
plt.figure(figsize=(10, 8))
sns.heatmap(df[['monthly_revenue', 'employee_count', 'project_duration', 'client_rating']].corr(), annot=True, cmap='YlGnBu')
plt.title("Correlation Matrix")
plt.show()

# 📈 Step 14: Monthly Revenue Trend (if date column exists)
if 'start_date' in df.columns:
    df['start_date'] = pd.to_datetime(df['start_date'])
    df_sorted = df.sort_values('start_date')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='start_date', y='monthly_revenue', data=df_sorted)
    plt.title("Monthly Revenue Trend Over Time")
    plt.xlabel("Start Date")
    plt.ylabel("Revenue (₹ lakhs)")
    plt.xticks(rotation=45)
    plt.show()

# 📄 Step 15: Save EDA Summary to Text File (Optional for Documentation)
with open("eda_summary.txt", "w", encoding="utf-8") as f:
    f.write("📊 Summary Statistics:\n")
    f.write(df.describe().to_string())
    f.write("\n\n📌 Company Distribution:\n")
    f.write(df['company_name'].value_counts().to_string())
    f.write("\n\n📌 Delivery Status Distribution:\n")
    f.write(df['delivery_status'].value_counts().to_string())
print("📄 EDA summary saved to 'eda_summary.txt'")

print("🎉 EDA completed successfully.")


