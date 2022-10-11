from flask import Flask, request
import socket
import datetime

app = Flask(__name__)


@app.route('/')
def homepage():
    ts = datetime.datetime.now()
    return "This is a python app served from {} time is {}".format(socket.gethostname(), ts.strftime("%H:%M:%S, %d/%m/%y"))


@app.route('/index')
def indexpage():
    return 'This is the index page :)'


# @app.route("/hostname/")
# def return_hostname():
#     return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)
#

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
