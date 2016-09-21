#sim808获取定位数据
>python语言，树莓派小车

## 资料
> GNNS的AT代码有效，GPS的AT命令返回ERROR,原因未知
* [淘宝链接](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.qqHedH&id=533784908573&_u=l8cjafjfd3c)
* [可用AT命令](http://www.elecrow.com/wiki/index.php?title=SIM808_GPRS/GSM%2BGPS_Shield_v1.1)
* [python实例代码](https://pcdotfan.com/2016/07/11/simcom-gps-works-with-amap-degeocoding-service/)

##sim808 AT命令意义（GNSS）
* `AT`  波特率确认，开机后多发几次
* `AT+IPR=9600` 更改波特率
* `AT+ECHARGE=1` 充电
* `AT&W` 保存设置
* `AT+CPOWD=1` 关机
* `AT+CBC` 显示电量 百分比和电压
* `AT+CSQ` 查询GSM信号质量
* `AT+CGNSPWR=1` 打开GNSS Power
* `AT+CGNSSEQ` Define the last NMEA sentence that parsed
* `AT+CGNSINF` GNSS navigation information parsed from NMEA sentences
* `AT+CGNSTST` Send data received from GNSS to AT UART

|Message |Description |Possible Talker Identifiers|
|--------|:--------------:|-------------------------:|
|GGA     |Time, position and fix type data| GP|
|GSA     |GNSS receiver operating mode, satellites used in the position solution, and DOP values| GP, GN|
|GSV |Number of GNSS satellites in view satellite ID numbers, elevation, azimuth, & SNR values |GP,GL,GN|
|RMC| Time, date, position, course and speed data| GP,GN|