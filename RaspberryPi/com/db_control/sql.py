# coding=utf-8

import sqlite3
import os

def db_init():
    if os.path.exists("./RaspberryPi.db"):pass
    else:
        os.system("sqlite3 ./RaspberryPi.db  < ./initdb.sql") #bug
    # db = sqlite3.connect("./RaspberryPi.db")
    # cu = db.cursor()
    # # cu.execute("CREATE TABLE IF NOT EXISTS hello (id INTEGER PRIMARY KEY,pid INTEGER,name VARCHAR(10) UNIQUE,nickname TEXT NULL)")
    # cu.execute("CREATE TABLE IF NOT EXISTS hello ("
    #            "id INTEGER PRIMARY KEY,"
    #            "texts VARCHAR(100),"
    #            "profilesId INTEGER NOT NULL,"
    #            "status INTEGER,"
    #            "weight INTEGER,"
    #            "CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')))")
    # cu.execute("CREATE TABLE IF NOT EXISTS jokes ("
    #            "id INTEGER PRIMARY KEY,"
    #            "texts VARCHAR(255),"
    #            "status INTEGER,"
    #            "CreatedTime TEXT)")
    # cu.execute("CREATE TABLE IF NOT EXISTS interaction ("
    #            "id INTEGER PRIMARY KEY,"
    #            "command VARCHAR(50),"
    #            "description VARCHAR(100),"
    #            "actionId INTEGER NOT NULL ,"
    #            "status INTEGER,"
    #            "CreatedTime TEXT)")
    # cu.execute("CREATE TABLE IF NOT EXISTS actions ("
    #            "id INTEGER PRIMARY KEY,"
    #            "description VARCHAR(100),"
    #            "status INTEGER,"
    #            "CreatedTime TEXT)")
    # cu.execute("CREATE TABLE IF NOT EXISTS helloProfiles ("
    #            "id INTEGER PRIMARY KEY,"
    #            "description VARCHAR(100),"
    #            "status INTEGER NOT NULL ,"  # 0失效，1可用，2随时可用
    #            "begintime TEXT,"
    #            "endtime TEXT,"
    #            "begindate TEXT,"
    #            "enddate TEXT)")  # 情景模式，设置hello表对应问候语的使用时间点。1为anytime
    # cu.execute("SELECT count(0) FROM hello")
    # if (cu.fetchone()[0] == 0):  # 默认问候语
    #     cu.execute("DELETE FROM helloProfiles")
    #     for t in [(u'随时可用', 2, '', '', '', ''), (u'早上使用', 1, '06', '10', '2017-09-06', '2017-09-30')]:
    #         cu.execute("INSERT INTO helloProfiles(description,status,begintime,endtime,begindate,enddate)"
    #                    " VALUES(?,?,?,?,?,?)", t)
    #     for t in [(u'HELLO WORLD', 1, 1, 60), (u'HELLO BOSS', 1, 1, 60), (u'早上好', 2, 1, 100), (u'一年之计在于晨', 2, 1, 100)]:
    #         cu.execute("INSERT INTO hello([texts],[profilesId],[status],[weight]) VALUES(?,?,?,?)", t)
    # cu.close()
    # db.commit()
    # db.close()


## 根据情景模式返还对应的问候语
def select_hello(time, status=1):
    __time = time
    __status = status
    try:
        db = sqlite3.connect("../db_control/RaspberryPi.db")
        cu = db.cursor()
        if __status == 2:
            cu.execute("SELECT h.texts,h.weight,h.id FROM hello h LEFT JOIN helloProfiles hp "
                       "WHERE h.profilesId=hp.id AND hp.status=2;")
            return cu.fetchall()
        else:
            cu.execute("SELECT h.texts,h.weight,h.id,hp.week FROM hello h LEFT JOIN helloProfiles hp "
                       "WHERE h.profilesId=hp.id AND hp.begintime<=? AND hp.endtime>? AND hp.status=1",
                       (__time, __time))
            return cu.fetchall()
    finally:
        cu.close()
        db.close()


def reduce_weight(id):
    __id = int(id)
    try:
        db = sqlite3.connect("../db_control/RaspberryPi.db")
        cu = db.cursor()
        cu.execute("UPDATE hello SET weight=20 WHERE id=?", (__id,))
        db.commit()
    finally:
        cu.close()
        db.close()


if __name__ == '__main__':
    db_init()
    reduce_weight(5)