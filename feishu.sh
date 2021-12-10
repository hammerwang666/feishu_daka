#sleep $[ ( $RANDOM % 200 )  + 1 ]

"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" runner "/Users/fanz/workspace/feishu_daka/feishu.air"  --device android://127.0.0.1:5037/$1?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH

