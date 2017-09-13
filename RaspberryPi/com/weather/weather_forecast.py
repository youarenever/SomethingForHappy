# coding=utf-8
import requests
import json

class weather_forecast_class():
    def __init__(self):
        pass

     ##调用第三天天气接口，处理后返回
    def weather_forecast_5days(self):
        data_5d_list = []
        weather_url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101010100"
        r = requests.get(weather_url)
        data_5d = json.loads(r.text)
        for i in range(5):
            tmp_list = []
            tmp_list.append(data_5d['data']['forecast'][i]['date'][-3:])
            tmp_list.append(data_5d['data']['forecast'][i]['date'][:-3])
            tmp_list.append(data_5d['data']['forecast'][i]['low'][3:-1] + "~" + data_5d['data']['forecast'][0]['high'][3:])
            tmp_list.append(data_5d['data']['forecast'][i]['type'])
            tmp_list.append(data_5d['data']['forecast'][i]['fengxiang'] + data_5d['data']['forecast'][0]['fengli'][10:-3])
            data_5d_list.append(tmp_list)
        data_5d_list.append(data_5d['data']['city'])
        data_5d_list.append(data_5d['data']['ganmao'])
        return data_5d_list

if __name__ == '__main__':
    a = weather_forecast_class()
    print a.weather_forecast_5days()[0][0]