# coding=utf-8
from RaspberryPi.com.db_control.sql import select_hello,reduce_weight
from time import strftime,gmtime
import random

class hello_world_main():
    def __init__(self):
        pass

    def hello(self):
        ##根据时间选择符合的问候语，并筛选权重最大的
        chour = int(strftime("%H"))
        #print type(chour)
        hello_tuple = select_hello(chour,2)
        if len(hello_tuple)==0:
            hello_tuple = select_hello(chour,2)
        tmp_weight= []
        for i in range(len(hello_tuple)):
            ran=random.random()
            tmp_weight.append(float(hello_tuple[i][1])*float(ran))
        # print tmp_weight
        max_weight_hello = tmp_weight.index(max(tmp_weight))
        print hello_tuple[max_weight_hello][0]
        # reduce_weight(hello_tuple[max_weight_hello][2])    #降低已出现的问候语的权重
        return hello_tuple[max_weight_hello][0]
        

    def jokes(self):
        pass

    def news(self):
        pass

if __name__ =="__main__":
    h = hello_world_main() 
    h.hello()