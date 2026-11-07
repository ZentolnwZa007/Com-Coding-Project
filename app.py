from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="pages",
    static_folder="assets"
)

@app.route("/")
def home():
    return render_template("MainPage.html")

app.run(debug=True)