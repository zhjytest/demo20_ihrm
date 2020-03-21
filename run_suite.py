
"""
    功能:入口脚本
"""

#导包
import unittest

from app import BASE_DIR
from script.test_login import TestLogin
from script.test_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner

#创建套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))

#生成测试报告
file_report = BASE_DIR + '/report/report.html'
with open(file_report,'wb') as f:
    HTMLTestRunner(f,verbosity=2,title="ihrm测试报告",description="第一版开发完成").run(suite)
