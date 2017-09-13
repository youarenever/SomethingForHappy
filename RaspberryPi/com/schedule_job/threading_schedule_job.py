# coding=utf-8
import threading
from time import sleep

import schedule as schedule

from RaspberryPi.com.db_control.sql import reset_weight


def job_reset_db_weight():
    print "begin reset db job"
    reset_weight()
    print "complete reset db job"


def job_():
    pass


def schedule_list():
    # schedule.every(5).minutes.do(job)
    # schedule.every(5).seconds.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("20:25").do(job_reset_db_weight)
    while True:
        schedule.run_pending()


T1 = threading.Thread(target=schedule_list)


def schedule_operation():
    if T1.is_alive():
        pass
    else:
        T1.start()


if __name__ == '__main__':
    schedule_operation()
