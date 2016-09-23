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

##返回的GPS数据
单次 
```
+CGNSINF: 1,1,20160921235709.000,30.439608,114.427183,14.900,0.65,201.0,1,,1.2,1.6,0.9,,14,4,,,37,,
```

连续 
```
$GPGLL,3026.3577,N,11425.6279,E,235943.000,A,A*5B
$GPGSA,A,3,08,27,28,03,30,,,,,,,,2.68,1.36,2.31*0D
$GPGSV,4,1,14,11,77,051,16,01,72,134,22,07,63,219,14,30,58,285,27*71
$GPGSV,4,2,14,08,38,042,41,28,30,316,39,22,16,134,23,17,16,257,20*7E
$GPGSV,4,3,14,03,08,153,31,27,06,060,23,16,03,110,21,09,02,205,*7A
$GPGSV,4,4,14,13,01,313,,193,,,*75
$GPRMC,235943.000,A,3026.3577,N,11425.6279,E,0.00,5.73,210916,,,A*60
$GPVTG,5.73,T,,M,0.00,N,0.00,K,A*3C
$GPGGA,235944.000,3026.3577,N,11425.6279,E,1,5,1.36,42.8,M,-
```