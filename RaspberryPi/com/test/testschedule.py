# coding=utf-8

import threading
import schedule
import time


def job():
    print("I'm working...", time.ctime())
def job2():
    print ("22222222222", time.ctime())

def schedule1(x):
    print "xxxxx"
    schedule.every(5).minutes.do(job)
    schedule.every(5).seconds.do(job)
    schedule.every(2).seconds.do(job2)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    while True:
        schedule.run_pending()
        # time.sleep(4)

if __name__ == '__main__':
    t=threading.Thread(target=schedule1,args=(1,))
    t.start()


    for i in range(10):
        print "main func222"
        time.sleep(1)

