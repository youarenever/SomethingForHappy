#coding=utf-8

import os
import sqlite3



try:
   db = sqlite3.connect("./db_control/RaspberryPi.db")
   cu = db.cursor()
   cu.execute("UPDATE hello SET weight=(select defaultweight from hello where defaultweight='60') where defaultweight='60'")
   cu.execute("UPDATE hello SET weight=(select defaultweight from hello where defaultweight='100') where defaultweight='100'")
   db.commit()
finally:
   cu.close()
   db.close()
