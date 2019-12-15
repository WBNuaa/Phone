import pymysql
class User():
    
    def __init__(self,username, password):
        self.username = username
        self.photonumber = []
        self.password = password
        self.email = []
        #print(self.username)
    def queryInformation(self):#个人信息查询
        #连接数据库userinf
        db = pymysql.connect('localhost','root','3424011','userinf')
        #建立游标对象，并定义以字典的形式存储从数据库读取的数据
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        #数据库的SQL语法，按用户名查询
        sql = "select * from tb_user where username={!r}".format(self.username)
        #执行
        cursor.execute(sql)
        #读取数据
        self.data = cursor.fetchall()
        #提交命令
        db.commit()
        #关闭游标和数据库
        cursor.close()
        db.close()
        #print(self.data[0]['username'])
        return self.data
    def changeinformation(self,data):#修改个人信息
        db = pymysql.connect('localhost','root','3424011','userinf')
        cursor = db.cursor()
        sql = "update tb_user set username={!r}, password={},phonenumber={},email={} where number = {}".format(data['username'],data['password'],data['phonenumber'],data['email'],self.data[0]['number'])
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    def JudgeExist(self): #判断用户是否存在
        db = pymysql.connect('localhost','root','3424011','userinf')
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from tb_user"
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        print(data)
        for i in range(len(data)):
            if self.username == data[i]['username']:
                if self.password == data[i]['password']:
                    print(self.username)
                    return True
        return False
'''
if __name__ == '__main__':
    user = User('123','123456')
    #data = user.queryInformation()
    #print(data)
    #data = {'id': '0', 'username': 'bu', 'password': '123456', 'phonenumber': '112345678', 'email': '2342342', 'number': 3}
    #user.changeinformation(data)
    user.JudgeExist()
'''





        
    
    
    
