#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(4):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(2)

# def move(func):
    # for i in range(2):
        # print "I was at the %s! %s" %(func,ctime())
        # sleep(5)

# threads = []
t1 = threading.Thread(target=music,args=(u'myholyday',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)

class Aa():
    def __init__(self):
        if t1.is_alive():
            print('\nStill running\n')
        else:
            t1.start()
            print('\nCompleted\n')
    def fff(self):pass
    
class Bb():
    def __init__(self):
        t1.start()

    def fff(self):pass
    
if __name__ == '__main__':
    a=Aa()
    print "xxxxx"
    b=Aa()
    # for t in threads:
        # t.setDaemon(True)
        # t.start()
    # t.join()
    print "\n this mian %s\n" %ctime()