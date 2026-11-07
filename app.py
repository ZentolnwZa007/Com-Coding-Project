from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="pages",
    static_folder="assets"
)

@app.route("/")
def MainPage():
    return render_template("MainPage.html")

@app.route("/WelcomePage")
def transition():
    return render_template("Transition.html")

app.run(debug=True)