# -*- coding:utf-8 -*-

from pre import get_html as gh

url = "https://loj.ac/problem/"

index = [32, 33, 34, 28, 35]
title = ["### 题目描述\n", "### 输入格式\n", "### 输出格式\n", "### 样例\n", "### 数据范围与提示\n"]

def face(pid):
    html = gh(url + str(pid) + "/edit")
    lines = html.split('\n')
    for i in range(len(lines)):
        if lines[i] == "var editors = {":
            '''
            description = lines[i+1][32:-4]
            input_format = lines[i+2][33:-4]
            output_format = lines[i+3][34:-4]
            example = lines[i+4][28:-4]
            limit_and_hint = lines[i+5][35:-4]
            '''
            md = [title[j] + lines[i + j + 1][index[j] : -4].replace('\\u002', '/').replace('\\r\\n', '\n') for j in range(5)]
            break
    text = '\n'.join(md)
    return text

def limit(pid):
    html = gh(url + str(pid))
    lines = html.split('\n')
    for i in range(len(lines)):
        if lines[i] == '      <div class="row" style="margin-top: -15px">':
            Space = lines[i+1][lines[i+1].index('：')+1 : lines[i+1].index(' M')]
            Time = lines[i+2][lines[i+2].index('：')+1 : lines[i+2].index(' m')]
            break
    return Space,Time