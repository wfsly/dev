# coding: utf-8

"""
根据所抓取的校区教学楼页面,将页面中的教室id 和教室名称抓取出来,以字典的形式存入到json文件中
source dir: class_list_data/
des dir: building_room_data/

脚本完成
"""
import json
import os
import re

from bs4 import BeautifulSoup

FILE_DIR = '/home/wang/dev/spider/class_list_data/'
DES_DIR = '/home/wang/dev/spider/building_room_data/'
file_list = os.listdir(FILE_DIR) 
print file_list

for f in file_list:
    campus_id = f[0:-5].split('-')[0]
    building_id = f[0:-5].split('-')[1]
    print campus_id + ' ' + building_id

    temp_file = open(FILE_DIR + f, 'r')
    
    web = BeautifulSoup(temp_file)
    
    td_tag = web.find_all('td', text='教室')
    tr_tag = td_tag[0].parent
    
    option_tag = tr_tag.find_all('option')
    
    #第一个option内容是"请选择", 删掉"
    option_tag.pop(0)
    
    room_dict = {}
    
    for item in option_tag:
        key = item.attrs['value']
        value = []
        text = item.text
        room_id = re.findall('\d\d\d', text)
        if room_id.__len__() != 0:
            value.append(room_id[0])
            value.append(text)
            #room_dict[room_id[0]] = text
            room_dict[key] = value
    
    res_file = open(DES_DIR + campus_id + '-' + building_id +'.json', 'w')
    json.dump(room_dict, res_file)
    res_file.close()
    temp_file.close()
