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
