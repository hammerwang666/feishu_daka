# feishu_daka
feishu daka base on airtest

## Install
download and install [airtest](https://airtest.netease.com/download.html?download=mac/AirtestIDE-mac-1.2.12.dmg&&site=io)

## Get device serial number
- open airtest IDE
- import feishu_daka project
- run
- get the serial number from console panel

## Deploy
```
crontab -e
36 8 * * *  sh {path_to_feishu_daka}/feishu.sh {device_serial_no}
```

 
 

