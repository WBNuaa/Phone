import pymysql
class Manager:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def QueryUserInformation(self): #查询全部的用户信息
        #连接数据库
        db = pymysql.connect('localhost','root','3424011','userinf')
        #建立游标对象
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        #SQL语言对数据库进行操作
        sql = "select * from tb_user"
        #执行
        cursor.execute(sql)
        #获取全部数据
        self.data = cursor.fetchall()
        #提交修改
        db.commit()
        #关闭游标和数据库连接
        cursor.close()
        db.close()
        self.len=len(self.data) #统计数据的大小
        return self.data
    def IncreaseUser(self,data):
        db = pymysql.connect('localhost','root','3424011','userinf')
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "insert into tb_user values('0',{},{},{},{},{})".format(data['username'],data['password'],data['phonenumber'],data['email'],self.len+1)
        cursor.execute(sql)
        self.data = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
    def JudgeUser(self,data):
        for i in range(len(self.data)):
            if data['username'] == self.data[i]['username']:
                return True
        return False
if __name__ == '__main__':
    m=Manager('玉文瑶','123456')
    m.QueryUserInformation()
    

