# coding:utf-8
import unittest

import getpathInfo
import readConfig
import os
from BeautifulReport import BeautifulReport

# 用例路径
# case_path = os.path.join(os.getcwd(), "case", 'blog')
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
path = getpathInfo.get_Path() # 因为这个拿到的是一个list，所以我们应该循环
top_level_dir = r'D:\pycharm\test02\temp202001\case'
print('report_path', report_path)
print('path111', path)


def all_case():
    discover_list = []
    # 循环
    for case_path in path:
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=top_level_dir)
        print(discover)
        discover_list.append(discover)
    return discover_list


if __name__ == "__main__":

    for discovers in all_case():
        run = BeautifulReport(discovers)
        run.report(description='Beautiful Report', filename='report.html', log_path=report_path)