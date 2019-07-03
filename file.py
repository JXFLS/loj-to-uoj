# -*- coding:utf-8 -*-

# By Llf0703
# 创建目录

import os
import shutil


def make_dir(pid):
    if not os.path.exists('resource'):
        os.makedirs('resource')
    if os.path.exists('resource/'+str(pid)):
        shutil.rmtree('resource/'+str(pid))
    os.makedirs('resource/'+str(pid))


def get_dir(pid):
    return 'resource/'+str(pid)+'/'
