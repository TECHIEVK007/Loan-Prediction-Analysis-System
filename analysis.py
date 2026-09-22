import pandas as pd
import numpy as np


# ============================================================
# LOAN PREDICTION DATA ANALYSIS SYSTEM
# DATA CLEANING + ANALYSIS
# ============================================================


# ------------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------------

file_name = "loan_approval_dataset.csv.xlsx"

df = pd.read_excel(file_name)


# ------------------------------------------------------------
# CLEAN COLUMN NAMES
# ------------------------------------------------------------

# Removes unwanted spaces from column names
df.columns = df.columns.str.strip()


# ------------------------------------------------------------
# CLEAN TEXT VALUES
# ------------------------------------------------------------

text_columns = [
    "education",
    "self_employed",
    "loan_status"
]

for column in text_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# ------------------------------------------------------------
# REMOVE DUPLICATES
# ------------------------------------------------------------

df = df.drop_duplicates()


# ------------------------------------------------------------
# HANDLE MISSING VALUES
# ------------------------------------------------------------

numeric_columns = [
    "no_of_dependents",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value"
]


for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# Fill missing numerical values using median
for column in numeric_columns:

    df[column] = df[column].fillna(
        df[column].median()
    )


# Fill missing categorical values using mode
for column in text_columns:

    if df[column].isnull().any():

        df[column] = df[column].fillna(
            df[column].mode()[0]
        )


# ------------------------------------------------------------
# REMOVE INVALID RECORDS
# ------------------------------------------------------------

df = df[
    (df["income_annum"] >= 0) &
    (df["loan_amount"] >= 0) &
    (df["loan_term"] > 0) &
    (df["cibil_score"] >= 300) &
    (df["cibil_score"] <= 900)
]


# ------------------------------------------------------------
# STANDARDIZE LOAN STATUS
# ------------------------------------------------------------

df["loan_status"] = (
    df["loan_status"]
    .replace({
        "Approved": "Approved",
        "Rejected": "Rejected",
        "Y": "Approved",
        "N": "Rejected"
    })
)


# ------------------------------------------------------------
# DERIVED COLUMN - TOTAL ASSET VALUE
# ------------------------------------------------------------

df["total_assets_value"] = (
    df["residential_assets_value"] +
    df["commercial_assets_value"] +
    df["luxury_assets_value"] +
    df["bank_asset_value"]
)


# ------------------------------------------------------------
# LOAN TO INCOME RATIO
# ------------------------------------------------------------

df["loan_income_ratio"] = np.where(
    df["income_annum"] > 0,
    df["loan_amount"] / df["income_annum"],
    0
)

df["loan_income_ratio"] = (
    df["loan_income_ratio"]
    .round(2)
)


# ------------------------------------------------------------
# CIBIL CATEGORY
# ------------------------------------------------------------

def cibil_category(score):

    if score >= 750:
        return "Excellent"

    elif score >= 650:
        return "Good"

    elif score >= 550:
        return "Average"

    else:
        return "Poor"


df["cibil_category"] = (
    df["cibil_score"]
    .apply(cibil_category)
)


# ------------------------------------------------------------
# INCOME CATEGORY
# ------------------------------------------------------------

def income_category(income):

    if income < 3000000:
        return "Low"

    elif income < 6000000:
        return "Medium"

    elif income < 9000000:
        return "High"

    else:
        return "Very High"


df["income_category"] = (
    df["income_annum"]
    .apply(income_category)
)


# ------------------------------------------------------------
# RISK LEVEL
# ------------------------------------------------------------

def calculate_risk(row):

    score = 0

    if row["cibil_score"] >= 750:
        score += 3

    elif row["cibil_score"] >= 650:
        score += 2

    elif row["cibil_score"] >= 550:
        score += 1


    if row["loan_income_ratio"] <= 2:
        score += 2

    elif row["loan_income_ratio"] <= 4:
        score += 1


    if row["total_assets_value"] >= row["loan_amount"]:
        score += 2


    if score >= 5:
        return "Low Risk"

    elif score >= 3:
        return "Medium Risk"

    else:
        return "High Risk"


df["risk_level"] = df.apply(
    calculate_risk,
    axis=1
)


# ------------------------------------------------------------
# ELIGIBILITY STATUS
# ------------------------------------------------------------

def eligibility(row):

    if (
        row["cibil_score"] >= 600 and
        row["income_annum"] > 0 and
        row["loan_income_ratio"] <= 5
    ):
        return "Eligible"

    return "Not Eligible"


df["eligibility_status"] = (
    df.apply(
        eligibility,
        axis=1
    )
)


# ------------------------------------------------------------
# BASIC ANALYSIS
# ------------------------------------------------------------

total_applicants = len(df)

approved_loans = (
    df["loan_status"] == "Approved"
).sum()

rejected_loans = (
    df["loan_status"] == "Rejected"
).sum()


approval_percentage = round(
    (
        approved_loans /
        total_applicants
    ) * 100,
    2
)


rejection_percentage = round(
    (
        rejected_loans /
        total_applicants
    ) * 100,
    2
)


average_income = round(
    df["income_annum"].mean(),
    2
)


average_loan = round(
    df["loan_amount"].mean(),
    2
)


average_cibil = round(
    df["cibil_score"].mean(),
    2
)


average_loan_term = round(
    df["loan_term"].mean(),
    2
)


# ------------------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------------------

print("\n============================================")
print("LOAN PREDICTION DATA ANALYSIS SYSTEM")
print("============================================")

print("\nTotal Applicants:", total_applicants)

print(
    "Approved Loans:",
    approved_loans
)

print(
    "Rejected Loans:",
    rejected_loans
)

print(
    "Approval Percentage:",
    approval_percentage,
    "%"
)

print(
    "Rejection Percentage:",
    rejection_percentage,
    "%"
)

print(
    "\nAverage Annual Income:",
    average_income
)

print(
    "Average Loan Amount:",
    average_loan
)

print(
    "Average CIBIL Score:",
    average_cibil
)

print(
    "Average Loan Term:",
    average_loan_term
)


print("\nEducation Distribution")

print(
    df["education"]
    .value_counts()
)


print("\nSelf Employment Distribution")

print(
    df["self_employed"]
    .value_counts()
)


print("\nRisk Distribution")

print(
    df["risk_level"]
    .value_counts()
)


print("\nCIBIL Categories")

print(
    df["cibil_category"]
    .value_counts()
)


# ------------------------------------------------------------
# SAVE PROCESSED DATASET
# ------------------------------------------------------------

df.to_csv(
    "processed_loans.csv",
    index=False
)


print(
    "\nProcessed dataset saved successfully:"
)

print(
    "processed_loans.csv"
)