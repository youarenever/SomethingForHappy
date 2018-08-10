# coding=UTF-8
from random import randint
import sqlite3

from flask import Flask, request, jsonify, Response, make_response

app = Flask(__name__)


def select_db(sql):
    conn = sqlite3.connect('mock.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return values


@app.route('/register', methods=["POST"])
def register():
    try:
        res = {"code": "9999", "msg": "服务器错误"}
        r = request.get_json()
        mobile = r["mobile"]
        pwd = r["pwd"]
        sql = 'select * from userinfo where mobile="' + mobile + '"'
        result = select_db(sql)
        if len(result) > 0:
            res["code"] = "1111"
            res["msg"] = "用户已注册"
        if mobile:      #判断手机号是否正确
            if len(pwd)==6:     #判断密码是否6位
                sql_in='insert into userinfo ("mobile","pwd") values ("'+ mobile +'","'+ pwd+'")'
                select_db(sql_in)
                res["code"] = "0000"
                res["msg"] = "注册成功"
            else:
                res["code"] = "1112"
                res["msg"] = "密码必须6位"
        else:
            res["code"] = "1113"
            res["msg"] = "手机号不正确"
    except:
        pass
    finally:
        rsp = make_response(jsonify(res))
        rsp.mimetype = 'application/json'
        return rsp

@app.route('/login', methods=["POST"])
def login():
    try:
        res = {"code": "9999", "msg": "服务器错误"}
        cookie = ""
        r = request.get_json()
        mobile = r["mobile"]
        pwd = r["pwd"]
        sql = 'select * from userinfo where mobile="' + mobile + '"'
        result = select_db(sql)
        if len(result) > 0:
            print(result)
            if str(pwd) == str(result[0][2]):
                for j in range(0, 20):
                    ran = randint(50, 90)
                    if ran > 65:
                        cookie = cookie + chr(ran)
                    else:
                        cookie = cookie + str(randint(0, 9))
                res["code"] = "0000"
                res["msg"] = "登录成功"
                sql_up = 'update userinfo set cookie ="' + cookie + '" where mobile="' + mobile + '"'
                select_db(sql_up)
            else:
                res["code"] = "2222"
                res["msg"] = "账户名或密码错误"
        else:
            res["code"] = "3333"
            res["msg"] = "用户未注册"
    except:
        pass
    finally:
        rsp = make_response(jsonify(res))
        rsp.mimetype = 'application/json'
        if len(cookie)>10:
            rsp.set_cookie('login', cookie)
        return rsp

@app.route('/addproduct', methods=["POST"])
def register():
    try:
        res = {"code": "9999", "msg": "服务器错误"}
        r = request.get_json()
        productid = r["productid"]
        number = r["number"]
        sql = 'select * from product where productid="' + productid + '"'
        result = select_db(sql)
        if len(result) > 0:
            sql_in = 'update product set num="'+number +'" where productid="'+productid+'"'
            select_db(sql_in)
            res["code"] = "0000"
            res["msg"] = "增加成功"
        else:
            productname=r["productname"]
            sql_in =  'insert into product ("productid","productname","num") values ("'+ productid +'","'+ productname+'","'+ number+'")'
            select_db(sql_in)
            res["code"] = "0000"
            res["msg"] = "增加成功"
    except:
        pass
    finally:
        rsp = make_response(jsonify(res))
        rsp.mimetype = 'application/json'
        return rsp



if __name__ == '__main__':
    # hello_world()
    app.run(debug=True, port=8999)
