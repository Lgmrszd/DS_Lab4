import time

import redis
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.add_url_rule('/favicon.ico',
                 redirect_to=url_for('static', filename='favicon.ico'))


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
    return render_template("index.html", visit_counts=0)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
