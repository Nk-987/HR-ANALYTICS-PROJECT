import pandas as pd

# Load dataset
df = pd.read_csv("data/hr_raw.csv")

print("Initial Shape:", df.shape)

# -------------------------
# 1. DATA CLEANING
# -------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# -------------------------
# 2. FEATURE ENGINEERING
# -------------------------

# Convert Attrition to numeric
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Create Age Groups
df['AgeGroup'] = pd.cut(df['Age'],
                       bins=[18, 25, 35, 45, 60],
                       labels=['18-25', '26-35', '36-45', '45+'])

# Create Income Levels
df['IncomeLevel'] = pd.cut(df['MonthlyIncome'],
                          bins=[0, 3000, 7000, 15000, 50000],
                          labels=['Low', 'Medium', 'High', 'Very High'])

# -------------------------
# 3. BASIC ANALYSIS
# -------------------------

# Overall attrition rate
attrition_rate = df['Attrition'].mean()
print("\nAttrition Rate:", round(attrition_rate * 100, 2), "%")

# Attrition by department
dept_attrition = df.groupby('Department')['Attrition'].mean()
print("\nAttrition by Department:\n", dept_attrition)

# Attrition by income level
income_attrition = df.groupby('IncomeLevel')['Attrition'].mean()
print("\nAttrition by Income Level:\n", income_attrition)

# -------------------------
# 4. SAVE CLEAN DATA
# -------------------------

df.to_excel("outputs/hr_cleaned.xlsx", index=False)

print("\n✅ Cleaned dataset saved successfully!")