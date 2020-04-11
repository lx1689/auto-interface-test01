# import json
# import unittest
# import urllib
#
# from common.configHttp import RunMain
# import geturlParams
# import readExcel
#
# url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
# login_xls = readExcel.readExcel().get_xls('userLoginCase.xlsx', 'vipList')
#
# class configResult(unittest.TestCase):
#     def testResult(self,path,query,method,case_name,description, returnCode):
#         # 用例描述
#         url1 = url + path
#         new_url = url1 + "?" + query
#         if query == '':
#             new_url = url1
#         data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}，字典形式form表单
#         info = RunMain().run_main(method, url1, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
#         ss = json.loads(info)  # 将响应转换为字典格式
#
#         self._testMethodName = case_name
#         self._testMethodDoc = description
#         self.assertEqual(ss['code'], returnCode)