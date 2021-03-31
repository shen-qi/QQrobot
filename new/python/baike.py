#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:34:39 2021

@author: yuan
"""

import urllib.request
import urllib.parse 
from lxml import etree

def baike(item = '你好'):
    baike_url = 'https://baike.baidu.com/item/' + urllib.parse.quote(item)
    print(baike_url)
    headers = {
            'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
            }
    item_req = urllib.request.Request(url = baike_url, headers=headers, method = 'GET')
    text = urllib.request.urlopen(item_req).read().decode('UTF-8')
    html = etree.HTML(text)
    sen_list = html.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()') 
    sen_list_after_filter = [item.strip('\n') for item in sen_list]
    return ''.join(sen_list_after_filter)
                   
if __name__ == '__main__' :
    print(baike('单处理系统'))
