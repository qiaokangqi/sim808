##sim808 AT命令
* AT+CBC 显示电量 百分比和电压
* 获取GPS的AT指令
```
    AT+CGPSPWR=1 #开启GPS的Power
    AT+CGPSRST=1 #设置GPS启动模式(COLD\HOT\WARM)，冷启动是第一次启动用
    AT+CGPSINF=32 #数据格式为GPRMC格式
```