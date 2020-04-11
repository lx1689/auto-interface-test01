import json
import unittest
from csv import excel
import ddt
import json
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel
from BeautifulReport import BeautifulReport as bf  #导入BeautifulReport模块，这个模块也是生成报告的模块


url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userLoginCase.xlsx', 'news')


@paramunittest.parametrized(*login_xls)
# @ddt.ddt
class testNews(unittest.TestCase):

    def setParameters(self, case_name, path, query, method, description, returnCode):
        """
        set params
        :param case_name: 用例名称
        :param path 请求路径
        :param query 请求参数
        :param method 请求方式
        :param description 用例描述
        :param returnCode 返回状态值
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.description = str(description)
        self.returnCode = returnCode

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")


    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    # @ddt.data(*login_xls)
    def testResult(self):  # 断言

        url1 = url + self.path
        new_url = url1 + "?" + self.query
        if self.query=='':
            new_url = url1
        data1 = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}，字典形式form表单
        info = RunMain().run_main(self.method, url1, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式

        self._testMethodName = self.case_name
        self._testMethodDoc = self.description
        self.assertEqual(ss['code'], self.returnCode)

