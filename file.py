# By Llf0703
# 创建目录

import os


def make_dir(pid):
    if not os.path.exists('resource'):
        os.makedirs('resource')
    if not os.path.exists('resource/'+str(pid)):
        os.makedirs('resource/'+str(pid))


def get_dir(pid):
    return 'resource/'+str(pid)+'/'
