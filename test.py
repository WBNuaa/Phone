#数据库的接口
import pymysql

config = {
    'host':'localhost',
    'user':'root',
    'password':'3424011',
    'database':'userinf'
}
#连接数据库
db = pymysql.connect('localhost','root','3424011','userinf')

#使用cursor()创建一个游标对象
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
#使用execute()执行SQL语句
cursor.execute("insert into tb_user values ('0','wen','123456','123456','123456')")
#sql = "update tb_user set username={!r} where number = {}".format('wen',3)
#sql = "select * from tb_user where username={!r}".format('bujidao')
#sql = "update tb_user set username={!r}, password={},phonenumber={},email={} where number = {}".format('wen','123456','123456','123456',3)
#cursor.execute(sql)
db.commit()
#使用fetchall()获取全部数据
#cursor.execute("select * from tb_user limit {}".format('3'))
data = cursor.fetchall()

print(data)

