from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    #weather = take from Vova
    return render_template("index.html", .....)

if __name__ == "__main__":
    app.run(debug = True)