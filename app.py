from flask import Flask, render_template, request
from modules.helper import fetch_data, programs_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", programs=programs_data())
    else:
        # Get the student ID, password, and program name from the form
        student_id = request.form["student_id"]
        password = request.form["password"]
        program_id = int(request.form["program"])

        return fetch_data(student_id, password, program_id, render_template)


@app.route("/privacy-policy", methods=["GET"])
def privacy_policy():
    return render_template("privacy.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
