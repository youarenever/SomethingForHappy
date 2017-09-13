# coding=utf-8
from flask import Flask, request, render_template
from RaspberryPi.com.home.helloworld import hello_world_main
from RaspberryPi.com.weather.weather_forecast import weather_forecast_class

app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin():
    hwm = hello_world_main()
    hello_message = hwm.hello()
    wf = weather_forecast_class()
    weather_message = wf.weather_forecast_5days()[0][0]
    return render_template('home.html', weathers=weather_message)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
