# -*- coding:utf-8 -*-

# By Terrasse
# 爬取题面及时空限制

from .pre import get_html as gh

url = "https://loj.ac/problem/"

index_pre = [32, 33, 34, 28, 35]
index_end = [-4, -4, -4, -4, -3]
title = ["### 题目描述\n", "\n### 输入格式\n","\n### 输出格式\n", "\n### 样例\n", "\n### 数据范围与提示\n"]
replace_list = [('\\u002f','/'), ('\\u002F','/'), ('\\u003e','>'), ('\\u003E','>'), ('\\r\\n','\n'), ('\\r','\n'), ('\\n','\n'), ('\\\\','\\')]


def get_face(pid):
    html = gh(url + str(pid) + "/edit")
    lines = html.split('\n')
    md = list()
    for i in range(len(lines)):
        if lines[i] == "var editors = {":
            for j in range(5):
                tmp = lines[i + j + 1][index_pre[j]: index_end[j]]
                if tmp != "":
                    for rpc in replace_list:
                        tmp = tmp.replace(rpc[0], rpc[1])
                    md += [title[j], tmp]
            break
    text = '\n'.join(md)
    return text


def get_limit(pid):
    html = gh(url + str(pid))
    lines = html.split('\n')
    for i in range(len(lines)):
        if lines[i] == '      <div class="row" style="margin-top: -15px">':
            Space = lines[i+1][lines[i+1].index('：')+1: lines[i+1].index(' M')]
            Time = lines[i+2][lines[i+2].index('：')+1: lines[i+2].index(' m')]
            break
    Time = str(round(int(Time)/1000))
    return Space, Time


def get_name(pid):
    html = gh(url + str(pid))
    lines = html.split('\n')
    return lines[11][11:-23]
