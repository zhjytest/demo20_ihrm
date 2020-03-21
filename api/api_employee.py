
"""
    功能：实现和员工管理相关的接口
"""
#导包
import requests
#创建类
from app import BASE_URL,headers_data


class ApiEmployee():

    def __init__(self):
        self.post_url = BASE_URL + "/api/sys/user"
        self.emp_url = BASE_URL + "/api/sys/user/{}"

    #员工添加
    def post_employee(self,mobile,username,work_number):
        emp_data = {"mobile":mobile,"username":username,"workNumber":work_number}
        response = requests.post(self.post_url,json=emp_data,headers=headers_data)
        result = response.json()
        result['status_code'] = response.status_code
        return result

    #员工查询
    def get_employee(self,emp_id):
        search_emp_url = self.emp_url.format(emp_id)
        response = requests.get(search_emp_url,headers=headers_data)
        result = response.json()
        result['status_code'] = response.status_code
        return result

    #员工删除
    def delete_employee(self,emp_id):
        del_emp_url = self.emp_url.format(emp_id)
        response = requests.delete(del_emp_url, headers=headers_data)
        result = response.json()
        result['status_code'] = response.status_code
        return result

    #员工修改
    def put_employee(self,username,emp_id):
        emp_data = {"username": username}
        put_emp_url = self.emp_url.format(emp_id)
        response = requests.put(put_emp_url, json=emp_data, headers=headers_data)
        result = response.json()
        result['status_code'] = response.status_code
        return result