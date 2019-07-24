# -*- coding:utf-8 -*-

# By Llf0703

import sys
from l2u.face import face
from l2u.upload import push
from l2u.file import make_dir
from l2u.testdata import testdata

if __name__ == '__main__':
    n = len(sys.argv)
    for i in range(1, n):
        pid = sys.argv[i]
        make_dir(pid)  # 创建目录
        testdata(pid)  # 下载及处理测试数据
        face(pid)  # 爬取题面
        push(pid) # 自动上传
