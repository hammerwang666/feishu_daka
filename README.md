# feishu_daka
feishu daka base on adb

## Install
- open debug mode on android phone
- connect to phone
- adb tcpip 5555

## Get device serial number
- adb devices

## Get feishu touch coordinate and replace in the daka.sh
- ex. adb -s $1 shell input tap 300 1464

## Deploy
```
crontab -e
36 8 * * *  sh {path_to_feishu_daka}/daka.sh {device_serial_no}
```

 
 

