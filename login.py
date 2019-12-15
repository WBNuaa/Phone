from User import User
from flask import Flask, request, render_template, redirect, url_for, abort, flash

app = Flask (__name__)
app.config['SECRET_KEY']='123456'
app.secret_key = '123456'
app.config.update(SECRET_KEY = '123456')

sum1 =0 #记录错误登录的次数
username ="" #记录登录的账号
password =""#记录登录的密码
phonenumber =[]#记录登录的手机号
email =[]#记录登录的邮箱

#登录界面
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST': #如果是注册操作，则保存注册的信息
        return render_template("login.html")
    else:
        return render_template("login.html")
#获取账号和密码进行判断
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        global username
        global password
        global sum1 # sum1发生修改所有要使用全部变量
        username = request.form.get('username')#获取name=username的inout输入框的值
        password = request.form.get('password')
        #print(username)
        if sum1<3:
            user = User(username,password)
            if not user.JudgeExist():
                sum1+= 1 #记录错误登录的次数
                print(sum1)
                flash("用户名或密码错误")
                return render_template("login.html")
            else:
                return redirect(url_for('personal'))#重定向为personal的地址，进行跳转
        else:
            abort(404)
#注册界面
@app.route('/signin',methods = ['GET','POST'])
def signin():
    return render_template("signin.html")
#个人中心界面
@app.route('/personal', methods = ['GET', 'POST'])
def personal():
    #使用字典传递个人信息，进行展示
    data = {
        "name": '文宝',
        "age" : '20'
    }
    return render_template("personal.html", data = data)
    


if __name__  == "__main__":
    app.run(debug = True)
