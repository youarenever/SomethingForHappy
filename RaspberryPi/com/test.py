#coding=utf-8

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

def init_db():
    db = sqlite3.connect("./test.db")
    cu = db.cursor()
    cu.execute("CREATE TABLE IF NOT EXISTS catalog (id INTEGER PRIMARY KEY,pid INTEGER,name VARCHAR(10) UNIQUE,nickname TEXT NULL)")
    # for t in [(0, 10, 'abc', 'Yu'), (1, 20, 'cba', 'Xu')]:
    #         db.execute("insert into catalog values (?,?,?,?)", t)
    # db.commit()

    cu.execute("select * from catalog")
    cu.execute("DELETE from catalog")
    db.commit()

    print cu.fetchall()
if __name__ == '__main__':
    init_db()


