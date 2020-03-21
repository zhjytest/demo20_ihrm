

#获取当前的路径
import os

CUR_DIR = os.path.abspath(__file__)
print(CUR_DIR)

BASE_DIR  = os.path.dirname(CUR_DIR)
print(BASE_DIR)

# TOKEN = "Bearer 03ff5627-f891-4f9f-9d99-bd106a0e3a19"
TOKEN = None
headers_data = {"Content-Type":"application/json","Authorization":TOKEN}


BASE_URL = "http://182.92.81.159/"