import dbHelp as db
from flask import Flask, render_template, request
# This is a sample Python script.
app = Flask(__name__)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def new_user():
    # 创建表完成
    # db.dbHelp().creat_table()
    user_name = input('请输入用户名称/n')
    user_password = input('请输入用户密码/n')
    result = db.dbHelp().insert_user(user_name,user_password)
    if result == True:
        print('数据插入完成')
    else:
        print('数据更新失败')

# Press the green button in the gutter to run the script.
def check_user():
    user_name = input('请输入需要查询的用户名：')
    result_check = db.dbHelp().check_user(user_name)
    if result_check == True:
        print('数据插入完成')
    else:
        print('数据更新失败')

#首页
@app.route('/index')
def index():
    return render_template("index.html")

# 用户注册页面
@app.route('/reg_user',methods=['get','post'])
def reg_page():
    return render_template("reg_user.html")
# 注册新用户数据处理
@app.route('/reg_check',methods=['get','post'])
def reg_check():
    req_data = request.args
    print(req_data)
    user_name = req_data.get('user_name')
    user_password = req_data.get('user_password')
    result_reg = db.dbHelp().insert_user(user_name,user_password)
    if result_reg == True:
        return "注册成功"
    else:
        return render_template("reg_user.html")

# 登陆验证
@app.route('/login',methods=['get','post'])
def login_page():
    return render_template('login.html')

# 登陆验证
@app.route('/login_check',methods=['get','post'])
def login_check():
    req_data = request.args
    user_name = req_data.get('user_name')
    user_password = req_data.get('user_password')
    result_check = db.dbHelp().login_check(user_name,user_password)
    if result_check == True:
        return '登陆成功，欢迎'+ user_name
    else:
        return '非法登陆，请检查用户名密码，或者注册新用户'
    db.cur.close()
    db.conn.close()


if __name__ == '__main__':
    print_hi('PyCharm')
    # print('1:新建用户。------2：查询用户')
    # select = input('请选择：')
    # if select == '1':
    #     new_user()
    # elif select == '2':
    #     check_user()
    # else:
    #     print('请正确选择！！！')
    app.run(host='0.0.0.0')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
