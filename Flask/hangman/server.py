from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
#PLACEHOLDER SECRET KEY
app.secret_key = "key_here"

@app.route("/")
def start_page():
    return render_template("start_page.html")

@app.route("/submit_word", methods=["post"])
def submit_word():
    # print(request.form["answer"])
    session["answer"] = request.form["answer"]
    progress = ""
    for i in range(0, len(request.form["answer"])):
        progress += "_"
    session["progress"] = progress
    # print(progress)
    session["incorrect"] = ""
    return redirect("/game")

@app.route("/game")
def game_page():
    return render_template("game.html")

@app.route("/submit_guess", methods=["post"])
def submit_guess():
    #do a lot of stuff with session
    guess = request.form["guess"].lower()
    print(guess)

    if(guess in session["answer"]):
        answer = session["answer"]
        progress = session["progress"]
        new_progress = ""

        for i in range(0,len(progress)):
            if progress[i] == "_" and answer[i] == guess:
                new_progress += guess
            elif progress[i] != "_":
                new_progress += progress[i]
            else:
                new_progress += "_"
        if new_progress == answer:
            return redirect("/win")
        session["progress"] = new_progress

        
    else:
        #add letter to incorrect
        session["incorrect"] += guess
        if len(session["incorrect"]) >= 6:
            return redirect("/lose")

    return redirect("/game")

@app.route("/lose")
def lose_page():
    return render_template("lose.html")

@app.route("/win")
def win_page():
    return render_template("win.html")

@app.route("/reset")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)