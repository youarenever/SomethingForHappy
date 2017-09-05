# coding=utf-8

import sqlite3


def db_init():
    db = sqlite3.connect("./test.db")
    cu = db.cursor()
    # cu.execute("CREATE TABLE IF NOT EXISTS hello (id INTEGER PRIMARY KEY,pid INTEGER,name VARCHAR(10) UNIQUE,nickname TEXT NULL)")
    cu.execute("CREATE TABLE IF NOT EXISTS hello ("
               "id INTEGER PRIMARY KEY,"
               "texts VARCHAR(100),"
               "status INTEGER,"
               "dates TEXT,"
               "time TEXT)")
    cu.execute("CREATE TABLE IF NOT EXISTS jokes ("
               "id INTEGER PRIMARY KEY,"
               "texts VARCHAR(255),"
               "status INTEGER,"
               "date TEXT,"
               "time TEXT)")
    cu.execute("CREATE TABLE IF NOT EXISTS interaction ("
               "id INTEGER PRIMARY KEY,"
               "command VARCHAR(50),"
               "description VARCHAR(100),"
               "actionId INTEGER,"
               "status INTEGER,"
               "dates TEXT)")
    cu.execute("CREATE TABLE IF NOT EXISTS action ("
               "id INTEGER PRIMARY KEY,"
               "description VARCHAR(100),"
               "status INTEGER,"
               "dates TEXT)")
