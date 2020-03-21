
"""
    功能:实现的是登录测试用例
"""

#导包
import logging
import unittest

from api.api_login import ApiLogin
from utils import common_assert
from app import TOKEN, headers_data, BASE_DIR
from parameterized import parameterized
import json


#读取参数化数据
#[(),(),()]
def build_data():
    test_data = []
    #读取data_login.json文件
    with open(BASE_DIR+'/data/data_login.json','r',encoding='utf-8') as f:
        datas = json.load(f)
        for d in datas:
            mobile = d.get('mobile')
            password = d.get('password')
            status_code = d.get('status_code')
            code = d.get('code')
            message = d.get('message')
            success = d.get('success')
            test_data.append((mobile,password,status_code,code,message,success))
    return test_data




#测试类
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login = ApiLogin()


    #登录参数化
    @parameterized.expand(build_data)
    def test_login(self,mobile,password,status_code,code,message,success):
        #初始化数据
        # mobile = "13800000002"
        # password = "123456"
        #请求接口
        res = self.login.login(mobile,password)
        logging.info("login data:{}".format(res))
        #断言
        # self.assertEqual(10000,res.get('code'))
        # self.assertEqual(True, res.get('success'))
        # self.assertEqual(200, res.get('status_code'))
        # self.assertIn("操作成功", res.get('message'))
        common_assert(self,res,status_code,code,message,success)

        #提取data的值
        str_data = res.get('data')
        if str_data:
            TOKEN = "Bearer " + str_data
            headers_data['Authorization'] = TOKEN


    #登录成功
    @unittest.skip
    def test_login_success(self):
        #初始化数据
        mobile = "13800000002"
        password = "123456"
        #请求接口
        res = self.login.login(mobile,password)
        logging.info("login data:{}".format(res))
        #断言
        # self.assertEqual(10000,res.get('code'))
        # self.assertEqual(True, res.get('success'))
        # self.assertEqual(200, res.get('status_code'))
        # self.assertIn("操作成功", res.get('message'))
        common_assert(self,res)

        #提取data的值
        str_data = res.get('data')
        if str_data:
            TOKEN = "Bearer " + str_data
            headers_data['Authorization'] = TOKEN



    #用户名为空
    @unittest.skip
    def test_username_is_null(self):
        #初始化数据
        mobile = ""
        password = "123456"
        #请求接口
        res = self.login.login(mobile,password)
        #断言
        # self.assertEqual(20001,res.get('code'))
        # self.assertEqual(False, res.get('success'))
        # self.assertEqual(200, res.get('status_code'))
        # self.assertIn("用户名或密码错误", res.get('message'))
        common_assert(self, res,200,20001,False,"用户名或密码错误")


    #密码为空
    @unittest.skip
    def test_password_is_null(self):
        #初始化数据
        mobile = "13800000002"
        password = ""
        #请求接口
        res = self.login.login(mobile,password)
        #断言
        # self.assertEqual(20001,res.get('code'))
        # self.assertEqual(False, res.get('success'))
        # self.assertEqual(200, res.get('status_code'))
        # self.assertIn("用户名或密码错误", res.get('message'))
        common_assert(self, res, 200, 20001, False, "用户名或密码错误")


    #用户名不存在
    @unittest.skip
    def test_usernam_is_not_exist(self):
        #初始化数据
        mobile = "10800000002"
        password = "123456"
        #请求接口
        res = self.login.login(mobile,password)
        #断言
        common_assert(self, res, 200, 20001, False, "用户名或密码错误")


    #密码错误
    @unittest.skip
    def test_password_is_error(self):
        #初始化数据
        mobile = "13800000002"
        password = "1234567"
        #请求接口
        res = self.login.login(mobile,password)
        #断言
        common_assert(self, res, 200, 20001, False, "用户名或密码错误")

    #请求参数为空
    @unittest.skip
    def test_params_is_null(self):
        #初始化数据
        mobile = None
        password = None
        #请求接口
        res = self.login.login(mobile,password)
        #断言
        common_assert(self, res, 200, 99999, False, "抱歉，系统繁忙，请稍后重试")

