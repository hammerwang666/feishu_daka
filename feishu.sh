sleep $[ ( $RANDOM % 720 )  + 1 ]
"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" runner "/Users/zf/workspace/feishu_daka/feishu.air"  --device android://127.0.0.1:5037/$1?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH

