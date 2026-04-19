from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/capitalize", methods=["GET", "POST"])
def capitalize():
    if request.method == "POST":
        name = request.form["name"]

        result = name.capitalize()

        return render_template("result39.html", result=result)

    return render_template("index39.html")

if __name__ == "__main__":
    app.run(debug=True)
