
"""
    实现的是员工管理场景用例
"""

#导包
import logging
import unittest,pymysql

#新建测试类
from api.api_employee import ApiEmployee
from utils import common_assert, Mysql
from parameterized import parameterized
import json
from app import BASE_DIR


def build_data(key_name,file_name=BASE_DIR+'/data/data_employee.json'):
    test_data = []
    with open(file_name,'r',encoding='utf-8') as f:
        datas = json.load(f)
        #logging.info("获取数据".format(datas))
        dict_data = datas.get(key_name)
        x = tuple(dict_data.values())
        logging.info("获取的值:{}".format(x))
        test_data.append(x)
    return test_data


#获取添加数据
def add_build_data():
    test_data = []
    with open(BASE_DIR+'/data/data_employee.json','r',encoding='utf-8') as f:
        datas = json.load(f)
        logging.info("获取数据:{}".format(datas))
        emp_data = datas.get('add_emp')
        x = (emp_data.get('mobile'),emp_data.get('username'),emp_data.get('work_number'),emp_data.get('status_code'),emp_data.get('code')
         ,emp_data.get('message'),emp_data.get('success'))
        test_data.append(x)
    return test_data

#获取查询数据
def search_build_data():
    test_data = []
    with open(BASE_DIR+'/data/data_employee.json','r',encoding='utf-8') as f:
        datas = json.load(f)
        logging.info("获取数据:{}".format(datas))
        emp_data = datas.get('search_emp')
        x = (emp_data.get('status_code'),emp_data.get('code'),emp_data.get('message'),emp_data.get('success'))
        test_data.append(x)
    return test_data


#获取修改数据
def update_build_data():
    test_data = []
    with open(BASE_DIR + '/data/data_employee.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)
        logging.info("获取数据:{}".format(datas))
        emp_data = datas.get('update_emp')
        x = (emp_data.get('username'),emp_data.get('status_code'), emp_data.get('code'), emp_data.get('message'), emp_data.get('success'))
        test_data.append(x)
    return test_data


#获取删除数据
def delete_build_data():
    test_data = []
    with open(BASE_DIR+'/data/data_employee.json','r',encoding='utf-8') as f:
        datas = json.load(f)
        logging.info("获取数据:{}".format(datas))
        emp_data = datas.get('delete_emp')
        x = (emp_data.get('status_code'),emp_data.get('code'),emp_data.get('message'),emp_data.get('success'))
        test_data.append(x)
    return test_data

class TestEmployee(unittest.TestCase):

    emp_id = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp = ApiEmployee()
        #cls.mobile = "13510002002"

    #员工添加
    @parameterized.expand(build_data("add_emp"))
    def test01_employee_add(self,mobile,username,work_number,status_code,code,message,success):
        #初始化数据

        # username = "test001"
        # work_number = "1000"
        #请求接口
        res = self.emp.post_employee(mobile,username,work_number)
        logging.info("add emp data:{}".format(res))
        #断言
        common_assert(self,res,status_code,code,message,success)
        #获取员工id
        TestEmployee.emp_id = res.get('data').get('id')


    #员工查询
    @parameterized.expand(build_data("search_emp"))
    def test02_employee_search(self,status_code,code,message,success):
        #请求接口
        res = self.emp.get_employee(TestEmployee.emp_id)
        logging.info("search emp data:{}".format(res))
        #断言
        common_assert(self,res,status_code,code,message,success)

    #员工修改
    @parameterized.expand(build_data("update_emp"))
    def test03_employee_update(self,username,status_code,code,message,success):
        #初始化数据
        #username = "test002"
        #请求接口
        res = self.emp.put_employee(username,TestEmployee.emp_id)
        logging.info("update emp data:{}".format(res))
        #断言
        common_assert(self,res,status_code,code,message,success)

        #连库操作
        # conn = pymysql.connect(host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm")
        # #创建连接
        # #创建游标
        # cursor = conn.cursor()
        # #执行SQL
        sql = "SELECT username from bs_user where id = '%s'" % (TestEmployee.emp_id)
        # cursor.execute(sql)
        # all_data = cursor.fetchone()[0]
        # logging.info("数据库查询结果:{}".format(all_data))
        #
        # #关闭游标
        # cursor.close()
        # #关闭连接
        # conn.close()
        all_data = Mysql().get_one(sql)[0]

        #断言
        self.assertEqual(username,all_data)


    # #员工查询
    # def test04_employee_search(self):
    #     #请求接口
    #     res = self.emp.get_employee(TestEmployee.emp_id)
    #     logging.info("search emp data:{}".format(res))
    #     #断言
    #     common_assert(self,res)


    #员工删除
    @parameterized.expand(build_data("delete_emp"))
    def test05_employee_delete(self,status_code,code,message,success):
        #请求接口
        res = self.emp.delete_employee(TestEmployee.emp_id)
        logging.info("delete emp data:{}".format(res))
        #断言
        common_assert(self,res,status_code,code,message,success)
