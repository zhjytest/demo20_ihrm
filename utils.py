import logging.handlers
from pathlib import Path
import os

#日志方法
import pymysql
import json
from app import BASE_DIR


#完成公共断言
def common_assert(test_case,result,status_code=200,code=10000,message='操作成功',success=True):
    test_case.assertEqual(status_code, result.get('status_code'))
    test_case.assertEqual(code, result.get('code'))
    test_case.assertEqual(success, result.get('success'))
    test_case.assertIn(message, result.get('message'))


#获取删除数据
def build_data(file_name,key_name):
    test_data = []
    with open(file_name,'r',encoding='utf-8') as f:
        datas = json.load(f)
        #logging.info("获取数据".format(datas))
        dict_data = datas.get(key_name)
        x = tuple(dict_data.values())
        logging.info("获取的值:{}".format(x))
        test_data.append(x)
    return test_data



def log_config():
    #创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #创建控制台输出器
    sh = logging.StreamHandler()
    #创建文件输出器
    log_dir = Path(BASE_DIR + '/log')
    print("log_dir:::",log_dir)
    if not log_dir.is_dir():
        os.mkdir(log_dir)
    log_file = os.path.join(log_dir,'ihrm.log')
    print("log_file:",log_file)
    th = logging.handlers.TimedRotatingFileHandler(log_file,when='midnight',interval=1,backupCount=7,encoding='utf-8')
    #创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    #把格式化器加入输出器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)
    #把输出器加入日志器
    logger.addHandler(sh)
    logger.addHandler(th)


#实现数据库的操作类
class Mysql():

    def __init__(self):
        self.conn = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm")


    #获取一条数据
    def get_one(self,sql):

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchone()
        finally:
            self.conn.close()



if __name__ == '__main__':

    z = build_data(BASE_DIR+'/data/data_employee.json','add_emp')
    print(z)
