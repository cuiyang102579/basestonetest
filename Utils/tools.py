# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 13:47
# @Software:basestonetest
# @File    : tools.py

import yaml
import pymysql
import redis


class YamlUtil:
    def __init__(self, yaml_file):
        """
        通过构造函数把yaml_file传入这个类
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        读取yaml，对yaml反序列化，把yaml格式转换成dict格式
        """
        with open(self.yaml_file, encoding="utf-8") as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value


class MySqlManager:
    """mysql管理器"""

    def __init__(self, db, user, passwd, host, port=3306, charset='utf8mb4'):
        """
        初始化数据库
        """
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__charset = charset
        self.__connect = None
        self.__cursor = None

    def _connect_db(self):
        """
        连接数据库
        """
        params = {
            "db": self.__db,
            "user": self.__user,
            "passwd": self.__passwd,
            "host": self.__host,
            "port": self.__port,
            "charset": self.__charset,
        }
        # cursorclass=pymysql.cursors.DictCursor 字典类型
        self.__connect = pymysql.connect(**params, cursorclass=pymysql.cursors.DictCursor)
        self.__cursor = self.__connect.cursor()

    def select(self, query, isOne=True):
        """
        直接传入sql语句获取结果
        """
        self._connect_db()
        self.__cursor.execute(query)
        if isOne:
            result = self.__cursor.fetchone()
        else:
            result = self.__cursor.fetchall()
        self._close_db()
        return result

    def _close_db(self):
        """
        关闭连接
        """
        self.__cursor.close()
        self.__connect.close()
'''
class MySQLServer:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")

        cur = self.conn.cursor(as_dict=True)
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
'''

class MyRedis:
    def __init__(self, ip, passwd, port=6379, db=0):
        # 构造函数
        try:
            self.r = redis.Redis(host=ip, password=passwd, port=port, db=db)

        except Exception as e:
            print('redis连接失败，错误信息%s' % e)

    def str_get(self, k):
        res = self.r.get(k)
        if res:
            return res.decode()

    def str_set(self, k, v, time=None):
        self.r.set(k, v, time)

    def delete(self, k):
        tag = self.r.exists(k)  # 判断这个Key是否存在
        if tag:
            self.r.delete(k)
            print('删除成功')
        else:
            print('这个key不存在')

    def hash_hget(self, name, key):
        res = self.r.hget(name, key)
        if res:
            return res.decode()

    def hash_hset(self, name, k, v):
        self.r.hset(name, k, v)

    def hash_getall(self, name):
        res = self.r.hgetall()
        new_dict = {}
        if res:
            for k, v in res.items():
                k = k.decode()
                v = v.decode()
                new_dict[k] = v
        return new_dict

    def hash_del(self, name, k):
        res = self.r.hdel(name, k)
        if res:
            print('删除成功')
            return True
        else:
            print('删除失败.该key不存在')
            return False

    @property
    def clean_redis(self):
        self.r.flushdb()  # 清空redis
        print('清空redis成功.')
        return 0


if __name__ == '__main__':
    YamlUtil("/Users/mac/Downloads/code/tasks_proj/tests/func/test_task.yaml").read_yaml()
    dbManager = MySqlManager(
        "库名",
        "账号",
        "密码",
        host="xxx",
    )
    cx = dbManager.select("SELECT * FROM xx limit 1;", False)


