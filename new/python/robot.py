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

encoding = 'utf-8'
BUFSIZE = 1024


# a read thread, read data from remote
class Reader(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        
    def run(self):
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
                print(strings)
                if 'user_id' in strings:

                    rec = eval(strings)
                    print(rec)
                    if '宝贝' in strings:
                        message = '宝贝个呸'
                        qq = rec['user_id']
                        url = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'.format(qq,message)
                        r = requests.get(url)
                        print(r.text)
                if 'group_id' in strings:
                    rec = eval(strings)
                    qq = rec['group_id']
                    print(rec)
                    if 'Kevin' in strings:
                        message = '我在这呢，现在我有以下功能哦！\n1.查看钉钉作业上交情况'
                        r = requests.get(url)
                        print(r.text)
                    if '查看钉钉作业上交情况'in strings:
                        message = linuxdd.job.dd()
                    url = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(qq,message)
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


lst  = Listener(8888)   # create a listen thread
lst.start() # then start
