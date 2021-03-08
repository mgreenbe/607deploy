from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def main():
    X, y = load_boston(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_tr, y_tr)
    joblib.dump(model, "boston.joblib")


if __name__ == "__main__":
    main()
