## this project is to grab the classroom data from "jw.qdu.edu.cn"

## including get authentication of jw, grab campus data, grab building data, grad room data 
## and classroom data.and parse them into .json file to load into django sqlite database

# Install virtualenv
## and then install requests, BeautifulSoup in the virtual development env

## about the captcha from jw, I used django view to get it and response it to browser to see it,
## and print JSESSIONID to get it

## Run

### 1.run grab_list_of_classroom.py to get room id

### 2.run parse_room_list.py to parse room id into .json

### 3.run grab_classroom_info.py to get daily using status of each room

### 4.run parse.py to parse room using info into .json

## classroom_info.json stored the data of campus and buildings, it is not the completed version

## Attention: in each .py script, it need to open files from dir, and you need to create the dir or change dir's name in script 
