# Loan Prediction Analysis System

<p align="center">
  <b>Data Analysis • Machine Learning • Flask • Android</b>
</p>

<p align="center">
  A complete academic loan analytics and prediction project with a responsive web dashboard and Android application.
</p>

<p align="center">
  <b>Designed and Developed by Sahu Tech</b>
</p>

---

## Overview

The **Loan Prediction Analysis System** is a complete data analysis and prediction project developed for academic use.

The system analyzes loan applicant data, performs preprocessing and financial analysis, builds a machine learning model, and presents the results through a responsive Flask web application and Android WebView application.

### Core Capabilities

- Data cleaning and preprocessing
- Loan approval analysis
- Financial statistics
- CIBIL score analysis
- Risk-level estimation
- Eligibility analysis
- Machine learning prediction
- Searchable applicant records
- Responsive dashboard
- Android WebView application

---

## System Architecture

```text
Dataset
   ↓
Python Data Analysis
   ↓
Processed Dataset
   ↓
Machine Learning Model
   ↓
Flask Backend
   ↓
Responsive Web Application
   ↓
Android WebView Application
```

---

## Technology Stack

### Data Analysis
- Python
- Pandas
- NumPy
- OpenPyXL

### Machine Learning
- Scikit-learn
- Logistic Regression
- OneHotEncoder
- ColumnTransformer
- Train/Test Split

### Backend
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Android
- Kotlin
- Android Studio
- Android WebView

### Development Tools
- Visual Studio Code
- Android Studio
- Git
- GitHub

---

## Dataset

The project uses a loan approval dataset containing approximately **4,269 applicant records**.

### Original Features

```text
loan_id
no_of_dependents
education
self_employed
income_annum
loan_amount
loan_term
cibil_score
residential_assets_value
commercial_assets_value
luxury_assets_value
bank_asset_value
loan_status
```

---

## Data Processing

The `analysis.py` module performs the primary data-processing workflow.

### Processing Steps

1. Load the Excel dataset
2. Clean column names
3. Standardize categorical values
4. Remove duplicate records
5. Convert numerical columns
6. Handle missing values
7. Validate financial data
8. Calculate derived financial metrics
9. Analyze CIBIL categories
10. Determine applicant risk levels
11. Determine basic eligibility
12. Generate statistical insights
13. Export the processed dataset

The processed output is saved as:

```text
processed_loans.csv
```

---

## Derived Features

### Total Assets Value

```text
Residential Assets
+ Commercial Assets
+ Luxury Assets
+ Bank Assets
```

### Loan-to-Income Ratio

```text
Loan Amount / Annual Income
```

### CIBIL Categories

| CIBIL Score | Category |
|---|---|
| 750 and above | Excellent |
| 650 - 749 | Good |
| 550 - 649 | Average |
| Below 550 | Poor |

### Income Categories

| Annual Income | Category |
|---|---|
| Below ₹30,00,000 | Low |
| ₹30,00,000 - ₹59,99,999 | Medium |
| ₹60,00,000 - ₹89,99,999 | High |
| ₹90,00,000 and above | Very High |

---

## Risk Analysis

The project performs basic rule-based risk evaluation using:

- CIBIL score
- Loan-to-income ratio
- Total asset value
- Loan amount

Applicants are classified as:

```text
Low Risk
Medium Risk
High Risk
```

> This risk classification is intended only for project-level analysis and demonstration.

---

## Loan Eligibility

Basic eligibility is determined using factors such as:

- CIBIL score
- Annual income
- Loan-to-income ratio

Eligibility results are classified as:

```text
Eligible
Not Eligible
```

---

## Machine Learning Model

The system uses **Logistic Regression** for loan-status prediction.

### Preprocessing Pipeline

Categorical features:

```text
education
self_employed
```

are transformed using:

```text
OneHotEncoder
```

Numerical features are passed through the preprocessing pipeline.

### Training Split

```text
80% Training Data
20% Testing Data
```

Model accuracy is calculated when the Flask application starts.

### Prediction Features

```text
no_of_dependents
education
self_employed
income_annum
loan_amount
loan_term
cibil_score
residential_assets_value
commercial_assets_value
luxury_assets_value
bank_asset_value
```

The model predicts:

```text
Approved
or
Rejected
```

---

## Web Application

The Flask application contains multiple pages.

### Dashboard

Displays:

- Total applicants
- Approved loans
- Rejected loans
- Approval rate
- Average income
- Model accuracy
- Loan status distribution
- Financial insights

### Applicants

Provides a searchable table of processed applicant records.

### Applicant Details

Displays detailed information for a selected applicant.

### Analysis

Shows analytical insights including:

- Loan status distribution
- CIBIL analysis
- Income analysis
- Risk distribution
- Financial metrics

### Prediction

Allows users to enter applicant details and obtain a prediction.

Additional outputs include:

- Predicted loan status
- Total assets
- Loan-to-income ratio
- CIBIL category
- Risk level
- Eligibility status

---

## Android Application

The project includes an Android application developed using:

- Kotlin
- Android Studio
- WebView

The app loads the Flask web interface inside a native Android application.

### Local Testing

The Flask backend must be running and accessible from the Android device.

Example:

```text
http://192.168.x.x:5000
```

For local testing, the computer and Android device should be connected to the same network.

### Important APK Note

The APK currently depends on the Flask backend.

Installing the APK alone does not make the complete system standalone.

For public distribution, the Flask backend should be deployed online and the Android WebView URL should be changed to the deployed HTTPS address.

---

## Project Structure

```text
Loan-Prediction-Analysis-System/
│
├── analysis.py
├── app.py
├── processed_loans.csv
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── dashboard.html
│   ├── applicants.html
│   ├── applicants_details.html
│   ├── analysis.html
│   └── prediction.html
│
└── Android App/
    ├── app/
    │   ├── src/
    │   ├── build.gradle.kts
    │   └── .gitignore
    │
    ├── gradle/
    ├── build.gradle.kts
    ├── gradle.properties
    ├── gradlew
    ├── gradlew.bat
    └── settings.gradle.kts
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/TECHIEVK007/Loan-Prediction-Analysis-System.git
cd Loan-Prediction-Analysis-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Data Analysis

```bash
python analysis.py
```

This generates:

```text
processed_loans.csv
```

### 4. Start the Flask Application

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

For another device on the same network:

```text
http://YOUR_LOCAL_IP:5000
```

---

## Android Setup

1. Open the `Android App/` folder in Android Studio.
2. Allow Gradle to synchronize.
3. Open `MainActivity.kt`.
4. Set the WebView URL to the running Flask server.

Example:

```kotlin
webView.loadUrl("http://192.168.x.x:5000")
```

5. Build and run the application on an Android device.

---

## Requirements

### Software

- Python 3.x
- Visual Studio Code or another Python IDE
- Android Studio
- Git

### Python Libraries

```text
Flask
pandas
numpy
scikit-learn
openpyxl
```

---

## Main Features

- Loan dataset preprocessing
- Financial data validation
- Duplicate removal
- Missing-value handling
- CIBIL score classification
- Income classification
- Loan-to-income calculation
- Asset-value calculation
- Risk-level analysis
- Eligibility analysis
- Loan approval statistics
- Machine learning prediction
- Responsive web dashboard
- Searchable applicant records
- Individual applicant details
- Android application
- Mobile-friendly interface

---

## Academic Purpose

This project was developed as a **Data Analysis Essentials academic project**.

The workflow demonstrates:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Processing
      ↓
Exploratory Analysis
      ↓
Machine Learning
      ↓
Web Application
      ↓
Mobile Application
```

The machine learning model and rule-based risk analysis are intended for educational and demonstration purposes.

---

## Future Enhancements

- Public cloud deployment
- Online database integration
- User authentication
- Admin dashboard
- Advanced machine learning models
- Model comparison
- Real-time analytics
- Interactive charts
- PDF report generation
- Loan application tracking
- REST API integration
- Standalone mobile backend integration
- Secure HTTPS deployment

---

## Repository

**GitHub:**  
https://github.com/TECHIEVK007/Loan-Prediction-Analysis-System

---

## Developer

### Sahu Tech

**Designed and Developed by Sahu Tech**

Focused on practical solutions in:

- Artificial Intelligence
- Machine Learning
- Data Analytics
- Software Development
- Web Applications
- Mobile Applications

---

## Disclaimer

This project is developed for **educational and academic purposes only**.

The predictions, risk classifications, eligibility results, and financial insights generated by this project should not be used as professional financial advice or as the sole basis for real-world lending decisions.

---

## License

This project is currently intended for educational and academic use.

---

<p align="center">
  <b>Loan Prediction Analysis System</b>
</p>

<p align="center">
  Data Analysis • Machine Learning • Flask • Android
</p>

<p align="center">
  Designed and Developed by <b>Sahu Tech</b>
</p>
