from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def contact_us():
    if request.method == "POST":
        name = str(request.form['name'])
        subject = str(request.form['subject'])
        email = str(request.form['email'])
        message = str(request.form['message'])
    else:
        return render_template("index.html")


@app.route('/post')
def post():
    return render_template("post.html")


if __name__ == '__main__':
    app.run()
