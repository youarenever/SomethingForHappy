# coding=utf-8
from flask import Flask, request, render_template

# from RaspberryPi.com.home.helloworld import hello_world_main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
