#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:43:44 2021

@author: yuan
"""
import requests
class group:
    def get_group_num():
        url = 'http://127.0.0.1:5700/get_group_list'
        r = requests.get(url).text
        dict = eval(r)
        return len(dict["data"])
    
    def get_group_id():
        url = 'http://127.0.0.1:5700/get_group_list'
        r = requests.get(url).text
        dict = eval(r)
        group_id_list = []
        for i in range(0,len(dict["data"])):
            group_id_list.append(dict["data"][i]['group_id'])
        return group_id_list
