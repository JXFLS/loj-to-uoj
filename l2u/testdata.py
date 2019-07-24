# -*- coding:utf-8 -*-

# By Llf0703
# 下载及处理测试数据

import os
import urllib
import requests
from .file import get_dir
from .info import get_limit


def get_testdata(pid):
    now_dir = get_dir(pid)
    url = 'https://loj.ac/problem/'+str(pid)+'/testdata/download'
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, now_dir+'data.zip')  # 下载压缩包
    os.system('cd '+now_dir+' && unzip data.zip -d data/')  # 解压
    os.remove(now_dir+'data.zip')  # 删除压缩包


def process_testdata(pid):
    now_dir = get_dir(pid)+'data/'  # 当前路径

    tests = os.listdir(now_dir)
    if len(tests) == 1:
        now_dir = now_dir + tests[0] + '/'  # 压缩文件夹下有子目录则进入

    tests = [name for name in os.listdir(now_dir)
             if os.path.isfile(os.path.join(now_dir, name)) and (os.path.splitext(name)[-1] == '.in' or os.path.splitext(name)[-1] == '.out' or os.path.splitext(name)[-1] == '.ans')]
    tests.sort()  # 所有输入输出文件
    data_num = len(tests)//2  # 测试点个数
    pre = os.path.splitext(tests[0])[0][:-1]  # 除去数字的前缀
    if pre == '':  # 无前缀则加前缀 data
        os.system('cd '+now_dir+' ; ls * | xargs rename \'s//data/\'')
        pre = 'data'
    os.system('cd '+now_dir+'; rename \'s/\.ans/.out/\' *')  # 将 .ans 转为 .out

    last_tests0 = tests[0]
    tests[0] = tests[0].replace('0', str(data_num))
    if tests[0] != last_tests0:  # 有 0.in/.out ，则将其重命名为 data_num.in/.out
        os.system('mv '+now_dir+pre+'0.in '+now_dir+pre+str(data_num)+'.in')
        os.system('mv '+now_dir+pre+'0.out '+now_dir+pre+str(data_num)+'.out')

    memory_limit, time_limit = get_limit(pid)  # 时空限制

    file = open(now_dir+'problem.conf', 'w')  # 写入 problem.conf
    file.write('use_builtin_judger on\n')
    file.write('use_builtin_checker wcmp\n')
    file.write('n_tests '+str(data_num)+'\n')
    file.write('n_ex_tests 0\n')
    file.write('n_sample_tests 0\n')
    file.write('input_pre '+pre+'\n')
    file.write('input_suf in\n')
    file.write('output_pre '+pre+'\n')
    file.write('output_suf out\n')
    file.write('time_limit '+time_limit+'\n')
    file.write('memory_limit '+memory_limit+'\n')
    file.write('output_limit 64')
    file.close()

    os.system('cd '+now_dir+' && zip -r uoj.zip *.in *.out *.conf')  # 打包成压缩包
    os.system('mv '+now_dir+'uoj.zip '+get_dir(pid))


def testdata(pid):
    print('downloading testdata...\n')
    get_testdata(pid)
    print('processing testdata...\n')
    process_testdata(pid)
