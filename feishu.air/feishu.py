# -*- encoding=utf8 -*-

from airtest.core.api import *
import json
import urllib.request
import urllib.parse
import sys
import time

nowDate = int(time.strftime("%Y%m%d", time.localtime()),10)
nowHour = int(time.strftime("%H", time.localtime()))

holiday_url = 'http://api.apihubs.cn/holiday/get'
f = urllib.request.urlopen(holiday_url)
body = f.read().decode('utf-8')
bodyObj = json.loads(body)
dateList = bodyObj["data"]["list"]
today =  [x for x in dateList if x["date"] == nowDate]

is_workday = today[0]["workday"]

if is_workday != 1:
    sys.exit()
    
keyevent("26")
keyevent("home")

stop_app('com.ss.android.lark')

sleep(5)
if exists(Template(r"tpl1646294491180.png", record_pos=(0.003, 0.896), resolution=(720, 1600))):
    touch(Template(r"tpl1646294516333.png", record_pos=(0.003, 0.986), resolution=(720, 1600)))
    
# start_app('com.ss.android.lark')



if exists(Template(r"tpl1668566245063.png", record_pos=(0.119, 0.886), resolution=(720, 1600))):
    touch(Template(r"tpl1668566245063.png", record_pos=(0.119, 0.886), resolution=(720, 1600)))

sleep(30)

if exists(Template(r"tpl1634293506221.png", record_pos=(0.011, 0.561), resolution=(1080, 1920))):
    touch(Template(r"tpl1634293519191.png", record_pos=(-0.209, 0.558), resolution=(1080, 1920)))

    


if exists(Template(r"tpl1633920745177.png", record_pos=(0.005, 0.039), resolution=(1080, 1920))):
    touch(Template(r"tpl1633920767258.png", record_pos=(0.005, 0.165), resolution=(1080, 1920)))
if exists(Template(r"tpl1633920811411.png", record_pos=(0.008, 0.047), resolution=(1080, 1920))):

    touch(Template(r"tpl1633920826053.png", record_pos=(-0.004, 0.252), resolution=(1080, 1920)))
    sleep(5) 
if exists(Template(r"tpl1632816183705.png", record_pos=(0.036, -0.147), resolution=(1080, 1920))):
    touch(Template(r"tpl1632816183705.png", record_pos=(0.036, -0.147), resolution=(1080, 1920)))
    if exists(Template(r"tpl1634608486464.png", record_pos=(0.195, 0.437), resolution=(1080, 1920))):
        touch(Template(r"tpl1634608486464.png", record_pos=(0.195, 0.437), resolution=(1080, 1920)))
        sleep(3)
if exists(Template(r"tpl1632813825231.png", record_pos=(0.027, 0.187), resolution=(1080, 1920))) and nowHour >= 18:
    if exists(Template(r"tpl1634608486464.png", record_pos=(0.195, 0.437), resolution=(1080, 1920))):
        touch(Template(r"tpl1634608486464.png", record_pos=(0.195, 0.437), resolution=(1080, 1920)))
        sleep(3)
    touch(Template(r"tpl1632813825231.png", record_pos=(0.027, 0.187), resolution=(1080, 1920)))

    
if exists(Template(r"tpl1634608412879.png", record_pos=(0.043, -0.144), resolution=(1080, 1920))):
    touch(Template(r"tpl1634608412879.png", record_pos=(0.043, -0.144), resolution=(1080, 1920)))
    if exists(Template(r"tpl1634608461124.png", record_pos=(0.008, 0.298), resolution=(1080, 1920))):
        touch(Template(r"tpl1634608486464.png", record_pos=(0.195, 0.437), resolution=(1080, 1920)))


    

sleep(5)

keyevent("home")
stop_app('com.ss.android.lark')

keyevent("26")
