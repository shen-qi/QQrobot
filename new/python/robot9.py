#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:27:15 2021
@author: yuan
"""

import threading
import socket
import requests
import re
import linuxdd
import json
import urllib.request
import mooc


encoding = 'utf-8'
BUFSIZE = 1024


# a read thread, read data from remote
class Reader(threading.Thread):
    def __init__(self, client):
        global chat
        threading.Thread.__init__(self)
        self.client = client
        
    def run(self):
        global chat    
    #用于字符串转变字典时的特殊定义
        true = 'true'
        null = 'null'
        #开始循环监听
        while True:
            data = self.client.recv(BUFSIZE)
            if(data):
                string = bytes.decode(data, encoding)
                #正则匹配
                strings = re.search('\{.*}', string).group()
                rec = eval(strings)
                if 'group_id' in strings:
                    qq = rec['group_id']
                    message = ''
                    mes = rec['raw_message']
                    if  '再见' in mes:
                        chat = 'Notallking'
                        message = chatter.tulin(mes)
                    if 'Kevin呢' in strings:
                        message = '我在这呢，现在我有以下功能哦！\n1.查看钉钉作业上交情况\n2.我们一起聊天吧'
                    if '查看钉钉作业上交情况'in strings:
                        message = linuxdd.job.dd()
                    if chat == 'Talking':
                        message = chatter.tulin(mes)
                    if chat == 'Searching':
                        message = mooc.mooc(mes)
                    if '我们一起聊天吧' in strings:
                        message = '你先说吧～'
                        chat = 'Talking'
                    if '搜题目' in strings:
                        chat = 'Searching'
                        message = 'Please tell me your question'

                    url = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(qq,message)
                    r = requests.get(url)
                    print(r.text)

                elif 'user_id' in strings:
                        if '宝贝' in strings:
                            message = '宝贝个呸'
                            qq = rec['user_id']
                            url = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(qq,message)
                            r = requests.get(url)
                            print(r.text)
            else:
                break
        print("close:", self.client.getpeername())
       
        
    def readline(self):
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, encoding)
            if len(string)>2:
                string = string[0:-2]
            else:
                string = ' '
        else:
            string = False
        return string


# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)
    def run(self):
        print("listener started")
        while True:
            client, cltadd = self.sock.accept()
            Reader(client).start()
            cltadd = cltadd
            print("accept a connect")

class chatter():
   def tulin(text_input):
        api_url = "http://openapi.tuling123.com/openapi/api/v2"
        req = {
            "perception":
            {
                "inputText":
                {
                    "text": text_input
                },
        
                "selfInfo":
                {
                    "location":
                    {
                        "city": "上海",
                        "province": "上海",
                        "street": "文汇路"
                    }
                }
            },
        
            "userInfo": 
            {
                "apiKey": "347b39ee228b4b109dae7270cc08d3c8",
                "userId": "OnlyUseAlphabet"
            }
        }
        # print(req)
        # 将字典格式的req编码为utf8
        req = json.dumps(req).encode('utf8')
        # print(req)
        
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        # print(response_str)
        response_dic = json.loads(response_str)
        # print(response_dic)
        
        intent_code = response_dic['intent']['code']
        results_text = response_dic['results'][0]['values']['text']
        return results_text
        
chat = 'Notalking'   
lst  = Listener(8888)   # create a listen thread
lst.start() # then start
