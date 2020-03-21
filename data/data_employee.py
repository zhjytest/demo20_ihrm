

assert_data = {"status_code": 200,"code": 10000,"message": "操作成功","success": True}
post_data = {"mobile":"13510002002","username":"test001","work_number":"1000"}
put_data = {"username":"test002"}

def gen_data(type='post'):
    if type in ['delete','get']:
        return list(assert_data.values())
    if 'put' == type:
        return list(put_data.values()) + list(assert_data.values())
    return list(post_data.values()) + list(assert_data.values())




if __name__ == '__main__':
    print(gen_data())

