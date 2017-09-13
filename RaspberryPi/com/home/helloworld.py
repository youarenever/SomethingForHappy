# coding=utf-8
from RaspberryPi.com.db_control.sql import select_hello, reduce_weight
from time import strftime, gmtime
import random

from RaspberryPi.com.schedule_job.threading_schedule_job import schedule_operation
from RaspberryPi.profiles_pi import *


class hello_world_main():
    def __init__(self):
        schedule_operation()
        pass

    def hello(self):
        ##根据时间选择符合的问候语，并筛选权重最大的
        chour = int(strftime("%H"))
        cweek = strftime("%w")
        # print type(cweek)
        # print type(chour)
        hello_tuple = select_hello(chour, 1)                #按时间条件筛选
        if len(hello_tuple) == 0:
            hello_tuple = select_hello(chour, 2)
        tmp_weight = []
        for i in range(len(hello_tuple) - 1, -1, -1):       #按星期条件筛选
            if str(hello_tuple[i][3]).find(cweek) < 0:
                hello_tuple.pop(i)
        for i in range(len(hello_tuple)):                   #按权重条件筛选
            ran = random.random()
            tmp_weight.append(float(hello_tuple[i][1]) * float(ran))
        # print tmp_weight
        max_weight_index = tmp_weight.index(max(tmp_weight))
        # print tmp_weight
        # print hello_tuple[max_weight_index][0]
        reduce_weight(hello_tuple[max_weight_index][2],20)  # 降低已出现的问候语的权重
        return YOUR_NAME + "," + hello_tuple[max_weight_index][0]

    def jokes(self):
        pass

    def news(self):
        pass


if __name__ == "__main__":
    h = hello_world_main()
    c = hello_world_main()
    print h.hello()
