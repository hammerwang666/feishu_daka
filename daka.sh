# crontab:
# 45 8 * * *  sh ~/workspace/feishu_daka/daka.sh EURC7S8STCNB9HA6
# 01 18 * * *  sh ~/workspace/feishu_daka/daka.sh EURC7S8STCNB9HA6

ip=172.63.52.114:5555

# 判断是否工作日
current_day=`date '+%Y%m%d'`
current_hour=`date '+%H'`
holiday_res=`curl -s "https://api.apihubs.cn/holiday/get?date=${current_day}&size=1&field=workday"`
is_workday=`echo ${holiday_res}|jq '.data.list[0].workday'`
if [ $is_workday == "0" ]
then 
 exit
fi

# 连接手机
adb connect $ip
# 唤醒
adb -s $1 shell input keyevent 26

# 启动飞书
adb -s $1 shell am start -n com.ss.android.lark/com.ss.android.lark.main.app.MainActivity
sleep 10s

# 打开工作台
adb -s $1 shell input tap 294 1459
sleep 10s

# 打开打卡应用
adb -s $1 shell input tap 265 881
sleep 30s

echo $current_hour

# 上班打卡
if [ $current_hour -lt 12 ]
then
 echo "上班打卡"
 adb -s $1 shell input tap 380 510
else
 echo "下班打卡"
 adb -s $1 shell input tap 389 785
fi
sleep 5s

# 打卡完成
adb -s $1 shell am force-stop com.ss.android.lark
adb -s $1 shell input keyevent 26
adb disconnect $ip
