import requests
import json
from common.loginSession import sessionRequest

class RunMain():

    def send_post(self, url, data):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = sessionRequest.post(url=url, json=data).json()  # 如果未做json转换则再转换一次
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = sessionRequest.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值错误！！！")
        return result


# if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
#     result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': ''})
#     result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111')
#     print(result1)
#     print(result2)