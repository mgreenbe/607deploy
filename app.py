from flask import Flask, redirect, render_template, request, url_for
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        x = request.form["x"]
        y = f"{2*float(x):.2f}"
        print(f"x={x}, y={y}")
        return redirect(url_for("index", x=x, y=y))
    x = request.args.get("x") or ""
    y = request.args.get("y") or ""
    return render_template("index.html", x=x, y=y)


@app.route("/telecom", methods=["GET", "POST"])
def telecom():
    print(request.method)
    if request.method == "POST":
        form_data = dict(request.form)
        x = process_form_data(form_data)
        y = model.predict([x])[0]
        print(f"x={x}, y={y}")
        return redirect(url_for("telecom", **form_data, y=y))
    return render_template("telecom.html", **request.args)


def process_form_data(form_data):
    gender = 1. if form_data["gender"] == "male" else 0.
    senior = 1. if form_data["senior"] == "yes" else 0.
    partner = 1. if form_data["partner"] == "yes" else 0.
    dependents = 1. if form_data["dependents"] == "yes" else 0.
    paperless = 1. if form_data["paperless"] == "yes" else 0.

    if form_data["payment"] == "electronic_check":
        payment = [1., 0., 0., 0.]
    elif form_data["payment"] == "mailed_check":
        payment = [0., 1., 0., 0.]
    elif form_data["payment"] == "credit_card":
        payment = [0., 0., 1., 0.]
    elif form_data["payment"] == "bank_transfer":
        payment = [0., 0., 0., 1.]
    else:
        raise Exception(f"Unknown payment method: {form_data['payment']}")

    if form_data["contract"] == "month_to_month":
        contract = [1., 0., 0.]
    elif form_data["contract"] == "one_year":
        contract = [0., 1., 0.]
    elif form_data["contract"] == "two_year":
        contract = [0., 0., 1.]
    else:
        raise Exception(f"Unknown contract type: {form_data['contract']}")

    tenure = float(form_data["tenure"])
    total = float(form_data["total"])
    monthly = float(form_data["monthly"])

    x = [gender, senior, partner, dependents, paperless, *payment,
         *contract, tenure, monthly, total]

    return x
