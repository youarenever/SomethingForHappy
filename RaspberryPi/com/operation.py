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
    weather_message0 = wf.weather_forecast_5days()[0]
    weather_message1 = wf.weather_forecast_5days()[1]
    weather_message2 = wf.weather_forecast_5days()[2]
    weather_message3 = wf.weather_forecast_5days()[3]
    weather_message4 = wf.weather_forecast_5days()[4]
    return render_template('home.html', hello=hello_message, weathers0=weather_message0, weathers1=weather_message1,
                           weathers2=weather_message2, weathers3=weather_message3, weathers4=weather_message4)
    # list1=[0,1,2,3,4,6,[3,40]]

    # return render_template('test.html',digits=list1[6])


if __name__ == '__main__':
    app.run(port=5001, debug=True)
