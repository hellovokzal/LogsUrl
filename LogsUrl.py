from flask import Flask, request
from os import *

logs = ""
num = 0

app = Flask(__name__)

@app.route('/')
def show_visitor_ip():
    global logs
    global num
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    num = num + 1
    system("clear")
    logs = f"{logs}\n{num}) {visitor_ip}"
    print(logs)
    return f'Ваш айпи: {visitor_ip}'

@app.route("/logs")

def logs():
    global logs
    system("clear")
    return logs

@app.route("/clear")

def clear():
    global logs
    logs = ""
    system("clear")
    return "Logs clearned"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
