from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/newnote/')
def newnote():
    return render_template("newnote.html")

if __name__ == "__main__":
    app.run(debug=True)