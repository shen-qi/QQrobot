#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:05:43 2021

@author: yuan
"""

import os
import pandas as pd
import time
import datetime
import pytz

class job:

 def dd():
    tz = pytz.timezone('Asia/Shanghai') #东八区
    t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    a = ""   
    #读取学号、姓名、宿舍号的excel表格 
    #路径
    xhpath = '~/Users/yuan/Documents/学号表.xlsx'
    newdf = pd.read_excel(xhpath, sheet_name="Sheet1")
    newdf = newdf[["姓名", "学号", "宿舍号"]] 
    
    #读取钉钉下载的 学生上传信息
    path = '/root/QQBOT/new/python/实验2'
    #读取文件夹下的所有文件名
    dirs = os.listdir(path)
    #初始化总共没交的人
    num = 0
    #初始化男生6个宿舍 n[1] - n [6]对应 301 302 303 304 305 306 
    #初始化 n[0] 给 女生
    n = [0,0,0,0,0,0,0]
    #遍历表中每一行的元素
    for i in range(0,42):
        #取出每一行的学号
        xh = newdf.loc[i]['学号']
        #用学号匹配文件夹下的所有文件名
        for name in dirs :
            #匹配到一个，即可以退出此循环
            if str(xh) in str(name) :
                break
        else:
            #如果学号匹配了所有都没有匹配成功，则这个学号的人没交作业
            #没交的总人数加1
            num = num + 1
            print(newdf.loc[i]['姓名'] + '还没有交作业哦!')
            #同时我们记录这个人的宿舍号
            sh = newdf.loc[i]['宿舍号']
            print(sh)
            #这个时候我用一个循环找到对应n[]的位置，并对此中数值加1
            for m in range(0,7):
                if '30'+ str(m) == str(sh) :
                    n[m] = n[m] + 1
                    break
            #我这里匹配了30开头的男生宿舍，如果全都未匹配成功则是女生宿舍
            else:
                    n[0] = n[0] + 1
    tm = '截止北京时间{0}\n'.format(t)
    a = a + tm 
    zj = 'Linux实训还有有' + str(num) + '人没交哦！\n'
    a = a + zj
    #循环打印宿舍没交的人数
    for i in range(0,7):
        if i == 0:
            ns = '女生还有{0}人未交\n'.format(n[0])
            a = a + ns
        else:
            ns = '30{0}还有{1}人未交\n'.format(str(i),n[i])
            a = a + ns
    return a 
if __name__ == '__main__' : 
    a = job.dd()
    print(a)
if __name__ == '__main__' : 
    job.dd()
    
