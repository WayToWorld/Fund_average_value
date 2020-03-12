#！-*-coding=utf-8-*-
from urllib import request,error
import re
import json
import time
from datetime import datetime

global null
null=''

#获取90天平均值
#url中应传入基金代码，页数，毫秒时间戳（可以省略）;每页90条数据
def GetData(fundCode,pageIndex):
	average=0.0
	url='http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18305814144381887112_1571732081658&fundCode='+fundCode+'&pageIndex='+pageIndex+'&pageSize=90&startDate=&endDate=&_=1571732081726'
	headers={ 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'  ,
                        'Referer':'http://fundf10.eastmoney.com/jjjz_001740.html' }
	req=request.Request(url=url,headers=headers)
	response=request.urlopen(req)
	data=response.read().decode('utf-8')
	data1=data[0:40]
	data2=re.search(r'\[.+\]',data).group()
	data3=data[-62:-2]
	UseData=eval(data2)
	for x in UseData:
		average+=((float)(x['DWJZ']))
	average=average/90
	return average
	#print average
#计算半年平均值
def HalfYearAverage(fundCode):
	TempValue = 0.0
	HalfAverage = 0.0
	for x in range(1,3):
		TempValue+=GetData(fundCode,str(x))
	HalfAverage=round(TempValue/2,3)
	return HalfAverage
#计算一年平均值
def YearAverage(fundCode):
	TempValue = 0.0
	YearAverage = 0.0
	for x in range(1,5):
		TempValue+=GetData(fundCode,str(x))
	YearAverage=round(TempValue/4,3)
	return YearAverage
	
'''
def RateChange(fundCode):
	HalfAverage=HalfAverage(fundCode)
	YearAverage=YearAverage(fundCode)
	HalfRateChange=(-HalfAverage)/HalfAverage
    YearRateChange=(-YearAverage)/YearAverage
'''
fundCode=input("请输入要计算的基金代码：")
YearAverage=YearAverage(fundCode)
print('该基金近|一年|平均单位净值为：',YearAverage)
HalfAverage=HalfYearAverage(fundCode)
print('该基金近|半年|平均单位净值为：',HalfAverage)
