# coding=utf-8
from RaspberryPi.com.db_control.sql import select_hello
from time import strftime,gmtime

class hello_world_main():
    def __init__(self):
        pass

    def hello(self):
        chour = int(strftime("%H"))
        #print type(chour)
        select_hello(chour)
        pass

    def jokes(self):
        pass

    def news(self):
        pass

if __name__ =="__main__":
    h = hello_world_main() 
    h.hello()