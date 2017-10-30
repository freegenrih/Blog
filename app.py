from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/post")
def post():
    return render_template('base/base.html')


@app.route("/contact")
def contact():
    return render_template('Contact.html')


@app.route("/about")
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)
