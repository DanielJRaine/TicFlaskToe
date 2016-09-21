"""Flask test."""
from flask import Flask, url_for, json, request, Response
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def api_root():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run()
