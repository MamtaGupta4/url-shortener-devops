from flask import Flask, render_template, request, redirect
from database import create_database, save_url, get_long_url
import random
import string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():

    long_url = request.form["long_url"]

    short_code = ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )

    save_url(long_url, short_code)

    # Automatically creates correct URL
    short_url = request.host_url + short_code

    return f"""
    <h2>✅ URL Shortened Successfully - Version 2</h2>

    <p><b>Original URL:</b></p>
    <p>{long_url}</p>

    <p><b>Short URL:</b></p>

    <a href="{short_url}" target="_blank">
        {short_url}
    </a>

    <br><br>

    <a href="/">← Create Another URL</a>
    """


@app.route("/<short_code>")
def redirect_url(short_code):

    result = get_long_url(short_code)

    if result:
        return redirect(result[0])

    return "<h2>❌ Short URL Not Found!</h2>"


if __name__ == "__main__":
    create_database()
    app.run(host="0.0.0.0", port=5000, debug=True)