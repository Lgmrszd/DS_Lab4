import time

import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_visit_counts():
    retries = 5
    while True:
        try:
            return cache.incr('visit_counts')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def index():
    visit_counts = get_visit_counts()
    return render_template("index.html", visit_counts=visit_counts)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
