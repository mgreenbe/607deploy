from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from joblib import dump


def main():
    X, y = datasets.load_breast_cancer(return_X_y=True)
    model = DecisionTreeClassifier()
    model.fit(X, y)
    dump(model, "model.joblib")


if __name__ == "__main__":
    main()
