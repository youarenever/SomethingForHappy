import sqlite3
mobile="13866661112"
pwd ="111111"
sql = 'insert into userinfo ("mobile","pwd") values ("'+ mobile +'","'+ pwd+'")'


def select_db(sql):
    conn = sqlite3.connect('mock.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return values

select_db(sql)
