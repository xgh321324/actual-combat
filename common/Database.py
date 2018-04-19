#coding:utf-8
import pymysql
from common.logger import Log
log = Log()

class Sqldriver(object):
    '''
    pymysql.Connect()参数说明
    host(str):      MySQL服务器地址
    port(int):      MySQL服务器端口号
    user(str):      用户名
    passwd(str):    密码
    db(str):        数据库名称
    charset(str):   连接编码

    connection对象支持的方法
    cursor()        使用该连接创建并返回游标
    commit()        提交当前事务
    rollback()      回滚当前事务
    close()         关闭连接

    cursor对象支持的方法
    execute(op)     执行一个数据库的查询命令
    fetchone()      取得结果集的下一行
    fetchmany(size) 获取结果集的下几行
    fetchall()      获取结果集中的所有行
    rowcount()      返回数据条数或影响行数
    close()         关闭游标对象
    '''
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # 执行Mysql查询
    def exec_mysql(self, sql):
        try:
            connect = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.database,
                                   charset='utf8'
                                   )
            #创建游标
            cur = connect.cursor()
            log.info(u"执行SQL语句|%s|" % sql)
            #执行sql
            cur.execute(sql)
            #提交事物
            connect.commit()
            log.info('成功影响了%s条数据' % cur.rowcount)
            values = cur.fetchall()
            print(values)
            return values
        except Exception as e:
            log.error('没有执行成功，原因是：%s' % e)
        finally:
            #关闭游标
            cur.close()
            #关闭连接
            connect.close()
            log.info('执行sql结束！')



if __name__=='__main__':
    s = Sqldriver('120.26.40.252',3306,'root','MedLander','school')
    sql = "select * from lesson"
    need = s.exec_mysql(sql)
    print('need:',need)
    print(len(need))
    for n in need:
        print(n[1])

