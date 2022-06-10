from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/second")
def second_page():
    print("secret message!!")
    return "this is the second page here!!!!"

@app.route("/repeat/<word>/<int:times>")
def repeater(word, times):
    return render_template("marquee.html", display=word, times=times)

if __name__ == "__main__":
    app.run(debug=True)