#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:20:53 2021

@author: yuan
"""

import requests

def mooc(question='你好'):
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 'xueqiu.com',
    'Referer': 'https//http://xueqiu.com/',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
    }
    mooc_url_api =  'http://imnu.52king.cn/api/wk/index.php?c='
    mooc_url_ans = mooc_url_api + question
    api_req = requests.get(mooc_url_ans,headers = headers)
    ans_dict = eval(api_req.text)
    answer = ans_dict['answer']
    return answer
    
if __name__ == "__main__":
    print(mooc())
