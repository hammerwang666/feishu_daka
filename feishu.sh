sleep $[ ( $RANDOM % 180 )  + 1 ]

"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" runner "/Users/fanz/workspace/feishu_daka/feishu.air"  --device android://127.0.0.1:5037/$1?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH --log "/var/folders/yh/pgyzl5vj7yb_t32ppz2zxmk80000gn/T/AirtestIDE/scripts/3e6426b9950d635cdbe75b1a4cc6ef4d"

