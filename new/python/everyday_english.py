#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:09:58 2021

@author: yuan
"""

import requests
import nowtime
import group 
def everyday_english():
    everyday_english_url = 'http://open.iciba.com/dsapi/'
    req = requests.get(everyday_english_url)
    dict_req_text = eval(req.text)
    content = dict_req_text['content']
    note = dict_req_text['note']
    format_content = content + '\n' +  note
    return format_content

if __name__ == '__main__':
    group_num =  group.group.get_group_num()
    group_id_list = group.group.get_group_id()
    for i in range(0,group_num): 
        qq = group_id_list[i]
        print(qq)
        message = nowtime.china() +  '\n' + '每日英语' + '\n'  + everyday_english()
        url = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(qq,str(message))
        print(url)
        r = requests.get(url)


