"""
Simple app for shortening URLs.
"""

import string
import random
from flask import request, redirect, Flask

app = Flask(__name__)
urls = {}


def generate_random_string() -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(6))


@app.post("/shrt")
def short_url() -> str:
    """
    Shorten a URL
    Takes a URL as a json parameter and returns a short URL.
    """
    try:
        url = request.json['url']
    except Exception:
        return "Error: No URL provided"
    if type(url) != str:
        return "Error: URL must be a string"
    rand_string = generate_random_string()
    new_url = f'localhost:5000/shrt/{rand_string}'
    urls[rand_string] = url
    return new_url


@app.get("/shrt/<short_url>")
def get_long_url(short_url):
    """
    Get the short URL and use it to redirect to the long URL
    params: short_url
    """
    try:
        old_url = urls[short_url]
    except Exception:
        return "URL not found"
    return redirect(old_url)


if __name__ == "__main__":
    app.run(debug=True)
