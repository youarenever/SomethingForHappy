# coding=utf-8

# from flask import Flask,request,render_template

# app = Flask(__name__)

# @app.route('/', methods=['GET','POST'])
# def home():
# return render_template('home.html')

# @app.route('/signin', methods=['GET'])
# def signin_form():
# return render_template('form.html')

# @app.route('/signin', methods=['POST'])
# def signin():
# username = request.form['username']
# password = request.form['password']
# if username=='admin' and password=='password':
# return render_template('signin_ok.html',username=username)
# return render_template('form.html',message='bad username or password',username=username)

# if __name__=='__main__':
# app.run(debug=True)

# coding=utf-8

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)