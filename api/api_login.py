
"""
    登录模块
        功能：实现跟登录相关的接口
        实现思路：
            1.新建类
            2.新建对应的测试方法，每个测试方法对应一个接口
"""

#导包
import requests
#登录类
from app import BASE_URL


class ApiLogin():


    def __init__(self):
        self.login_url  = BASE_URL + '/api/sys/login'


    #登录接口
    def login(self,mobile,password):
        login_data = {}
        response = None
        if mobile:
            login_data['mobile'] = mobile
        if password:
            login_data['password'] = password

        if login_data:
            #请求登录接口
            response = requests.post(self.login_url,json=login_data)
        else:
            response = requests.post(self.login_url)
        result = response.json()
        #status_code = response.status_code
        result['status_code'] = response.status_code
        return result


if __name__ == '__main__':
    lg = ApiLogin()
    print(lg.login("13800000002","123456"))



