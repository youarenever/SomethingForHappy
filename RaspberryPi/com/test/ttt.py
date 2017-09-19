# coding=utf-8
# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
# if __name__ == '__main__':
#     app.run(port=5001)
# import os
# path="F:\git\SomethingForHappy\RaspberryPi\com\db_control\RaspberryPi.db"
#
# print os.path.dirname(path)
# os.chdir("F:\\test")
# os.system("sqlite3 dd.db < initdb.sql")
list1 = [1, 3, 4, 5]
dict = {1: 11, 2: list1}


print dict[2]
