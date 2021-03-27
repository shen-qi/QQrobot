#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:28:51 2021

@author: yuan
"""

import os
import pandas as pd

#路径区
path = '/Users/yuan/Downloads/xyrsb'
dirs = os.listdir(path)
# =============================================================================
# print(dirs)
# =============================================================================
#利用区
new = path + '/' + '徐乙冉197701079.xls'
newdf = pd.read_excel(new, sheet_name="Sheet1")
newdf = newdf[["姓名", "项目 得分", "合计"]]
print(type(newdf))

#遍历文件
for i in dirs:
    print(i)
    if '.DS' in i :
        continue
    if i == '徐乙冉197701079.xls':
        continue
# =============================================================================
#     print(i)
# =============================================================================
    name = path+ '/' + i
# =============================================================================
#     print(name)
# =============================================================================
    df = pd.read_excel(name, sheet_name="Sheet1")
    df = df[["姓名", "项目 得分", "合计"]]
#删去NAN的合并单元格值
    df = df.dropna(axis=0,how='all')  
#连接表格
    newdf = pd.concat([newdf, df], axis=0)

#新建的表格，准备写入
new = path + '/' + 'new.xls'
# =============================================================================
# a = newdf.to_excel(new, index=0)
# =============================================================================
print(newdf)


