import sqlite3

conn = sqlite3.connect('parts.db',timeout=10,check_same_thread=False)
cur = conn.cursor()
class dbHelp:
    # conn = sqlite3.connect('parts.db')
    # cur = conn.cursor()
    # 创建用户信息表表
    def creat_table(self):
        sql_text_1 = '''CREATE TABLE user_info
                       (user_name TEXT,
                        user_password TEXT);'''
        cur.execute(sql_text_1)
        print(sql_text_1)
        return True

    # 在用户信息表中插入数据
    def insert_user(self,user_name,user_password):
        user = 'INSERT INTO user_info VALUES(' + user_name + ',' + user_password + ')'

        sql_0 = "insert into user_info values('" + user_name + "','" + user_password +"')"
        print(sql_0)
        # 执行语句

        cur.execute(sql_0)
        # 更新执行
        conn.commit()
        cur.close()
        conn.close()
        return True

    # 检查表中的数据
    def check_user(self,user_name):
        sql_check = 'select * from user_info where user_name = "' + user_name +'"'
        print(sql_check)
        a = cur.execute(sql_check)
        b = cur.fetchall()
        print(b)
        for row in b:
            print(row)

        cur.close()
        conn.close()
        return True

    # 检查登陆用户
    def login_check(self,user_name,user_password):
        sql_check = 'select * from user_info where user_name = "' + user_name + '" and user_password = "'+ user_password +'"'
        print(sql_check)
        a = cur.execute(sql_check)
        b = cur.fetchall()
        print(len(b))
        for row in b:
            print(row)

        if len(b) == 0:
            return False
        else:
            return True
