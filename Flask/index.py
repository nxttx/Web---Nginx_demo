import flask 
import os
import datetime

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello World! From python"

@app.route('/check')
def check():
    return "2"

@app.route('/time')
def time():
    return str(datetime.datetime.now()) + " from python"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))

    from waitress import serve
    serve(app, host='0.0.0.0', port=port)
    

