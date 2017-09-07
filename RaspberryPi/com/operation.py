# coding=utf-8
from flask import Flask, request, render_template

from RaspberryPi.com.home.helloworld import hello_world_main

app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin():
    hwm = hello_world_main()
    hello_message = hwm.hello()
    return render_template('home.html', message=hello_message )

if __name__ == '__main__':
    app.run(port=5002)