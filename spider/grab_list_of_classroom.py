# coding:utf-8
import requests
import json

#CAPTCHA_URL = 'http://jw.qdu.edu.cn/academic/getCaptcha.do'
#r = requests.get(CAPTCHA_URL)
#print r.cookies['JSESSIONID']
r = requests.Session()
r.cookies['JSESSIONID'] = 'EF65396357DF5A5E6853402BCAEBC48C.TAC1'

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
INDEX_URL = 'http://jw.qdu.edu.cn/academic/index_new.jsp'
content = r.get(INDEX_URL)

CLASSROOM_INFO_URL = 'http://jw.qdu.edu.cn/academic/teacher/teachresource/roomschedulequery.jsdo'
#CLASSROOM_INFO_URL = 'http://jw.qdu.edu.cn/academic/teacher/teachresource/roomschedule.jsdo'
fs = open('classroom_info.json', 'r')
data = json.load(fs)

for i in range(0, 2):
    dict_campus = data[i]
    building_list = dict_campus['building_dict']['buildings']
    campus_id = dict_campus['campus_id']
    for ele in building_list:
        building_id = ele['building_id']
        form = {
        'aid': campus_id,
        'buildingid': building_id
                }
        classroom_info = r.post(CLASSROOM_INFO_URL, data=form)
        print classroom_info.text
        file_name = campus_id + '-' + building_id + '.html'
        f = open('class_list_data/' + file_name, 'w')
        f.write(unicode.encode(classroom_info.text, 'utf-8'))
        f.close()
