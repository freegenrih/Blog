from flask import (Flask,
                   render_template,
                   url_for,
                   request,
                   redirect
                   )

from executors.Logic_post import POSTS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', post=POSTS().get())


@app.route("/post")
def post():
    return render_template('base/base.html')


@app.route("/contact")
def contact():
    return render_template('Contact.html')


@app.route("/about")
def about():
    return render_template('About.html')


@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        # print(request.form['text'])
        return render_template('Search.html', post=POSTS(search=str(request.form['text'])).search_text())
    else:
        return redirect(url_for("index"))



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

            debug=True )
