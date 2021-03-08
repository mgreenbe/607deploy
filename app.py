from flask import Flask
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")


@app.route('/')
def hello_world():
    y_pr = model.predict([range(30), range(1, 31), range(2, 32)])
    return 'Hello, World!\n' + str(y_pr)
