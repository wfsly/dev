# coding:utf-8
"""
根据提取的教学楼和教室编号,抓取对应教室的使用情况
"""
import json
import os
import requests

#CAPTCHA_URL = 'http://jw.qdu.edu.cn/academic/getCaptcha.do'
#r = requests.get(CAPTCHA_URL)
#print r.cookies['JSESSIONID']
r = requests.Session()
r.cookies['JSESSIONID'] = 'E66D6CF3E73BCF79A84B3C060CE1BD7F.TAC2'

LOGIN_URL = 'http://jw.qdu.edu.cn/academic/j_acegi_security_check'
USERNAME = '201340704074'
PASSWD = 'wandove8023@u'
CAPTCHA = input('input captcha:')

form_data = {
        'j_username': USERNAME,
        'j_password': PASSWD,
        'j_captcha': CAPTCHA
        }
content = r.post(LOGIN_URL, data=form_data)
print content.text
INDEX_URL = 'http://jw.qdu.edu.cn/academic/index_new.jsp'
content = r.get(INDEX_URL)
print content.text

#CLASSROOM_INFO_URL = 'http://jw.qdu.edu.cn/academic/teacher/teachresource/roomschedulequery.jsdo'
CLASSROOM_INFO_URL = 'http://jw.qdu.edu.cn/academic/teacher/teachresource/roomschedule.jsdo'

SOURCE_DIR = '/home/wang/dev/spider/building_room_data/'
DES_DIR = '/home/wang/dev/spider/room_info/'
file_list = os.listdir(SOURCE_DIR)

for f in file_list:
    form = {}
    campus_id = f[0:-5].split('-')[0]
    building_id = f[0:-5].split('-')[1]
    room_id = ''
    form['aid'] = campus_id
    form['building_id'] = building_id

    temp_file = open(SOURCE_DIR + f, 'r')
    room_dict = json.load(temp_file)
    #print room_dict
    for key in room_dict.keys():
        form['room'] = key
        room_id = room_dict[key][0]
        
        classroom_info = r.post(CLASSROOM_INFO_URL, data=form)
        #print classroom_info.text
        #f = open('/home/wang/res.html', 'w')
        #print type(campus_id)
        #print type(building_id)
        #print type(room_id)

        f = open(DES_DIR + campus_id + '-' + building_id + '-' + room_id + '.html', 'w')
        f.write(unicode.encode(classroom_info.text, 'utf-8'))
        f.close()
