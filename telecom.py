import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

URL = "https://raw.githubusercontent.com/mgreenbe/telecom/main/telecom_users.csv"


def main():
    df = pd.read_csv(URL, index_col="customerID")
    df.drop(columns=[df.columns[0]], inplace=True)
    df = df[df.TotalCharges != " "]
    y = (df.Churn.values == "Yes").astype(int)

    X = np.zeros((len(df), 15)).astype(float)

    X[:, 0] = df.gender == "Male"
    X[:, 1] = df.SeniorCitizen
    X[:, 2] = df.Partner == "Yes"
    X[:, 3] = df.Dependents == "Yes"
    X[:, 4] = df.PaperlessBilling == "Yes"

    X[:, 5] = df.PaymentMethod == "Electronic check"
    X[:, 6] = df.PaymentMethod == "Mailed check"
    X[:, 7] = df.PaymentMethod == "Credit card (automatic)"
    X[:, 8] = df.PaymentMethod == "Bank transfer (automatic)"

    X[:, 9] = df.Contract == "Month-to-month"
    X[:, 10] = df.Contract == "One year"
    X[:, 11] = df.Contract == "Two year"

    X[:, 12] = df.tenure
    X[:, 13] = df.MonthlyCharges
    X[:, 14] = df.TotalCharges.astype(float)

    model = DecisionTreeClassifier()
    model.fit(X, y)
    dump(model, "telecom.joblib")


if __name__ == "__main__":
    main()
