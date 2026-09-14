from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary attendance records
records = [
    {
        "name": "Juan Dela Cruz",
        "date": "September 14, 2026",
        "status": "Present"
    }
]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        status = request.form["status"]

        records.append({
            "name": name,
            "date": date,
            "status": status
        })

        return redirect("/")

    return render_template("index.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)