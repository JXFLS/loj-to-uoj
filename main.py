# -*- coding:utf-8 -*-

# By Llf0703

import sys
from face import face
from upload import push
from file import make_dir
from testdata import testdata

if __name__ == '__main__':
    n = len(sys.argv)
    for i in range(1, n):
        pid = sys.argv[i]
        make_dir(pid)  # 创建目录
        testdata(pid)  # 下载及处理测试数据
        face(pid)  # 爬取题面
        push(pid)
