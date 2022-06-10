from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/change_name", methods=["POST"])
def change_name():

    print("hey you're trying to change the name to: " + request.form["name"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
