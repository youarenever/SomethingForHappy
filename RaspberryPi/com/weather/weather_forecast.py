# coding=utf-8
import requests
import json

class weather_forecast_class():
    def __init__(self):
        pass

     ##调用第三天天气接口，处理后返回
    def weather_forecast_5days(self):
        # data_5d_dict = []
        data_5d_dict = {}
        weather_url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101020100"
        r = requests.get(weather_url)
        data_5d = json.loads(r.text)
        for i in range(5):
            tmp_list = []
            tmp_list.append(data_5d['data']['forecast'][i]['date'][-3:])
            tmp_list.append(data_5d['data']['forecast'][i]['date'][:-3])
            tmp_list.append(data_5d['data']['forecast'][i]['low'][3:-1] + "~" + data_5d['data']['forecast'][0]['high'][3:])
            tmp_list.append(data_5d['data']['forecast'][i]['type'])
            tmp_list.append(data_5d['data']['forecast'][i]['fengxiang'] + data_5d['data']['forecast'][0]['fengli'][10:-3])
            # data_5d_dict.append(tmp_list)
            data_5d_dict[i]=tmp_list

        # data_5d_dict.append(data_5d['data']['city'])
        # data_5d_dict.append(data_5d['data']['ganmao'])
        data_5d_dict["city"]=data_5d['data']['city']
        data_5d_dict["ganmao"]=data_5d['data']['ganmao']

        #根据天气判断返回对应的图片
        dict1={u"阴":"./yin.gif",u"小雨":"./xiaoyu.gif",u"晴":"./qing.gif",u"中雨":"./zhongyu.gif",u"大雨":"./dayu.gif",u"阵雨":"./zhenyu.gif"}
        tmp_list = []
        for i in range(5):
            if data_5d_dict[i][3] in dict1:
                tmp_list.append(dict1[data_5d_dict[i][3]])
            else:
                tmp_list.append("null")
        data_5d_dict["picturelist"]=tmp_list
        return data_5d_dict

if __name__ == '__main__':
    a = weather_forecast_class()
    dict1 = a.weather_forecast_5days()
    print dict1.keys()
