from flask import Flask, render_template, request
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# LOAD PROCESSED DATASET
# ============================================================

df = pd.read_csv(
    "processed_loans.csv"
)


# ============================================================
# MACHINE LEARNING MODEL
# ============================================================

features = [
    "no_of_dependents",
    "education",
    "self_employed",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value"
]


X = df[features]

y = df["loan_status"]


categorical_features = [
    "education",
    "self_employed"
]


numerical_features = [
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


preprocessor = ColumnTransformer(
    transformers=[
        (
            "category",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ],
    remainder="passthrough"
)


model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000
            )
        )
    ]
)


# ------------------------------------------------------------
# TRAIN / TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )
)


# ------------------------------------------------------------
# TRAIN MODEL
# ------------------------------------------------------------

model.fit(
    X_train,
    y_train
)


# ------------------------------------------------------------
# MODEL ACCURACY
# ------------------------------------------------------------

predictions = model.predict(
    X_test
)

model_accuracy = round(
    accuracy_score(
        y_test,
        predictions
    ) * 100,
    2
)


print(
    "Loan Prediction Model Accuracy:",
    model_accuracy,
    "%"
)


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
def dashboard():

    total_applicants = len(df)

    approved_loans = int(
        (
            df["loan_status"]
            == "Approved"
        ).sum()
    )

    rejected_loans = int(
        (
            df["loan_status"]
            == "Rejected"
        ).sum()
    )

    approval_rate = round(
        (
            approved_loans /
            total_applicants
        ) * 100,
        2
    )

    rejection_rate = round(
        100 - approval_rate,
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


    return render_template(
        "dashboard.html",

        total_applicants=total_applicants,

        approved_loans=approved_loans,

        rejected_loans=rejected_loans,

        approval_rate=approval_rate,

        rejection_rate=rejection_rate,

        average_income=average_income,

        average_loan=average_loan,

        average_cibil=average_cibil,

        model_accuracy=model_accuracy
    )


# ============================================================
# APPLICANTS PAGE
# ============================================================

@app.route("/applicants")
def applicants():

    applicant_data = (
        df.to_dict(
            orient="records"
        )
    )

    return render_template(
        "applicants.html",
        applicants=applicant_data
    )


# ============================================================
# APPLICANT DETAILS
# ============================================================

@app.route(
    "/applicant/<int:loan_id>"
)
def applicant_details(
    loan_id
):

    applicant = df[
        df["loan_id"] == loan_id
    ]

    if applicant.empty:

        return (
            "Applicant not found",
            404
        )

    applicant = (
        applicant.iloc[0]
    )

    return render_template(
        "applicants_details.html",
        applicant=applicant
    )


# ============================================================
# ANALYSIS PAGE
# ============================================================

@app.route("/analysis")
def analysis():

    approval_distribution = (
        df["loan_status"]
        .value_counts()
        .to_dict()
    )


    education_distribution = (
        df.groupby(
            "education"
        )["loan_status"]
        .value_counts()
        .unstack(
            fill_value=0
        )
        .to_dict(
            orient="index"
        )
    )


    self_employed_distribution = (
        df.groupby(
            "self_employed"
        )["loan_status"]
        .value_counts()
        .unstack(
            fill_value=0
        )
        .to_dict(
            orient="index"
        )
    )


    risk_distribution = (
        df["risk_level"]
        .value_counts()
        .to_dict()
    )


    cibil_distribution = (
        df["cibil_category"]
        .value_counts()
        .to_dict()
    )


    income_distribution = (
        df["income_category"]
        .value_counts()
        .to_dict()
    )


    return render_template(
        "analysis.html",

        approval_distribution=
        approval_distribution,

        education_distribution=
        education_distribution,

        self_employed_distribution=
        self_employed_distribution,

        risk_distribution=
        risk_distribution,

        cibil_distribution=
        cibil_distribution,

        income_distribution=
        income_distribution
    )


# ============================================================
# PREDICTION PAGE
# ============================================================

@app.route(
    "/prediction",
    methods=[
        "GET",
        "POST"
    ]
)
def prediction():

    result = None

    risk_level = None

    eligibility = None

    loan_income_ratio = None

    total_assets = None

    cibil_category = None


    if request.method == "POST":

        no_of_dependents = int(
            request.form[
                "no_of_dependents"
            ]
        )

        education = request.form[
            "education"
        ]

        self_employed = request.form[
            "self_employed"
        ]

        income_annum = float(
            request.form[
                "income_annum"
            ]
        )

        loan_amount = float(
            request.form[
                "loan_amount"
            ]
        )

        loan_term = float(
            request.form[
                "loan_term"
            ]
        )

        cibil_score = float(
            request.form[
                "cibil_score"
            ]
        )

        residential_assets = float(
            request.form[
                "residential_assets"
            ]
        )

        commercial_assets = float(
            request.form[
                "commercial_assets"
            ]
        )

        luxury_assets = float(
            request.form[
                "luxury_assets"
            ]
        )

        bank_assets = float(
            request.form[
                "bank_assets"
            ]
        )


        # ----------------------------------------------------
        # CREATE INPUT DATA
        # ----------------------------------------------------

        prediction_data = pd.DataFrame(
            [{
                "no_of_dependents":
                    no_of_dependents,

                "education":
                    education,

                "self_employed":
                    self_employed,

                "income_annum":
                    income_annum,

                "loan_amount":
                    loan_amount,

                "loan_term":
                    loan_term,

                "cibil_score":
                    cibil_score,

                "residential_assets_value":
                    residential_assets,

                "commercial_assets_value":
                    commercial_assets,

                "luxury_assets_value":
                    luxury_assets,

                "bank_asset_value":
                    bank_assets
            }]
        )


        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        result = model.predict(
            prediction_data
        )[0]


        # ----------------------------------------------------
        # TOTAL ASSETS
        # ----------------------------------------------------

        total_assets = (
            residential_assets +
            commercial_assets +
            luxury_assets +
            bank_assets
        )


        # ----------------------------------------------------
        # LOAN / INCOME RATIO
        # ----------------------------------------------------

        if income_annum > 0:

            loan_income_ratio = round(
                loan_amount /
                income_annum,
                2
            )

        else:

            loan_income_ratio = 0


        # ----------------------------------------------------
        # CIBIL CATEGORY
        # ----------------------------------------------------

        if cibil_score >= 750:

            cibil_category = (
                "Excellent"
            )

        elif cibil_score >= 650:

            cibil_category = (
                "Good"
            )

        elif cibil_score >= 550:

            cibil_category = (
                "Average"
            )

        else:

            cibil_category = (
                "Poor"
            )


        # ----------------------------------------------------
        # RISK LEVEL
        # ----------------------------------------------------

        score = 0

        if cibil_score >= 750:
            score += 3

        elif cibil_score >= 650:
            score += 2

        elif cibil_score >= 550:
            score += 1


        if loan_income_ratio <= 2:
            score += 2

        elif loan_income_ratio <= 4:
            score += 1


        if total_assets >= loan_amount:
            score += 2


        if score >= 5:

            risk_level = (
                "Low Risk"
            )

        elif score >= 3:

            risk_level = (
                "Medium Risk"
            )

        else:

            risk_level = (
                "High Risk"
            )


        # ----------------------------------------------------
        # ELIGIBILITY
        # ----------------------------------------------------

        if (
            cibil_score >= 600
            and income_annum > 0
            and loan_income_ratio <= 5
        ):

            eligibility = (
                "Eligible"
            )

        else:

            eligibility = (
                "Not Eligible"
            )


    return render_template(
        "prediction.html",

        result=result,

        risk_level=risk_level,

        eligibility=eligibility,

        loan_income_ratio=
        loan_income_ratio,

        total_assets=
        total_assets,

        cibil_category=
        cibil_category,

        model_accuracy=
        model_accuracy
    )


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )