# coding:utf-8
import json
import os
from bs4 import BeautifulSoup as bs

SOURCE_DIR = '/home/wang/dev/spider/room_info/'
DES_DIR = '/home/wang/dev/spider/data2/'

file_list = os.listdir(SOURCE_DIR)
for f in file_list:
    campus_id = f[0:-5].split('-')[0]
    building_id = f[0:-5].split('-')[1]
    room_id = f[0:-5].split('-')[2]
    temp_file = open(SOURCE_DIR + f, 'r')
    web = bs(temp_file)
    #f = open('1709-1904-303', 'r')

    result = web.find_all('table')
    #get the count of item from result, result is a list
    #result.__len__()
    
    #result.pop把第一个table(显示的是标题)删除掉
    result.pop(0)
    #后面的table成对处理,第一个table里内容是周数,第二个table里是这周对应的课表

    res = {}
    while result.__len__() != 0:
        table1 = result.pop(0)
        table2 = result.pop(0)
        #将第一个tr中的
        week_num = table1.td.string
        #获取table中的所有的tr,每行tr都是教室使用情况
        tr = table2.find_all('tr')
        #删除第一个tr内容(因为是星期标题)
        tr.pop(0)
        #存储一周13节课的教室使用情况
        week_res = []
        for item in tr:
            #td中是对应节次教室使用情况'√'有课, ' '无课 
            #temp存储一小节7天的使用情况
            week_temp = []
            td = item.find_all('td')
            for ele in td:
                if ele.string == ' ':
                    week_temp.append(0)
                else:
                    week_temp.append(1)
            week_res.append(week_temp)
    
        week_num = week_num[1:week_num.__len__()-1]
        res[week_num] = week_res
    
    #print res
    final = {}
    for i in res.keys():
        temp1 = []
        for j in range(0,7):
            temp2 = []
            for ele in res[i]:
                temp2.append(ele[j])
            temp1.append(temp2)
        final[i] = temp1
    
    
    #for i in res.keys():
    #    file_name = f.name + '-' + i + '.json'
    #    f2 = open('./data1/' + file_name, 'w')
    #    json.dump(res[i], f2)
    #    f2.close()
    #
    
    for i in final.keys():
        #file_name = f.name + '-' + i + '.json'
        file_name = campus_id + '-' + building_id + '-' + room_id + '-' + i + '.json'
        f2 = open(DES_DIR  + file_name, 'w')
        json.dump(final[i], f2)
        f2.close()
