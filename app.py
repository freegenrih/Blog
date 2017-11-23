from flask import Flask, render_template, url_for

from executors.Logic_post import POST

app = Flask(__name__)


@app.route("/")
def index():

    return render_template('index.html', post=POST().get())


@app.route("/post")
def post():
    return render_template('base/base.html')


@app.route("/contact")
def contact():
    return render_template('Contact.html')


@app.route("/about")
def about():
    return render_template('About.html')


# error hendler
def bad_request(e):
    return render_template('errors/400.html'), 400


def page_not_found(e):
    return render_template('errors/404.html'), 404


def page_error(e):
    return render_template('errors/500.html'), 500


app.register_error_handler(400, bad_request)
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, page_error)
# end error hendler
if __name__ == '__main__':
    app.run(#host='192.168.100.73',
            debug=True)
