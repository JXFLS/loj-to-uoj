# -*- coding:utf-8 -*-

# By Llf0703
# 创建题面 problem.md 文件

from file import get_dir
from info import get_face


def face(pid):
    file = open(get_dir(pid)+'problem.md', 'w')
    file.write(get_face(pid))
    file.close()
