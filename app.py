from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "屈凡哲" and password == "屈凡哲":
        return redirect(url_for('index'))
    else:
        return render_template('login.html', error="账号或密码错误！")

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)