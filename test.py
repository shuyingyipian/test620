# -*- coding: utf-8 -*-
# @Time : 2022-06-16 11:33
# @Author : lj
# @File : test.py
# @Software: PyCharm


from datetime import datetime

uri = "noiseVideo_2022-06-16-11-21-28_2022-06-16-11-21-38.mp4"

# 一行流pythonic，
pubtime = ''.join(uri.split('_')[1].split('-'))
print(pubtime)

lst = uri.split("_")
print(lst)

pubtime2 = lst[1].split("-")
print(pubtime2)
print(type(pubtime2))
# pubtime = lst[1].split("-")

# 转数字为时间，按时间格式作为字符串
from dateutil.parser import parse
tim = "".join(pubtime2)
c = parse(tim)  # tim为字符串类型：20220616112128
print(c)  # 2022-06-16 11:21:28

# pubtime = datetime.strptime(str(tim),'%Y%m%d %H%M%S')
# print(pubtime)

# dt = 20180908
# pubtime = datetime.strptime(str(dt), '%Y%m%d')
# print(dt)
#
#
# import pandas as pd
# pd.to_datetime('2018-09-08')
# #Timestamp('2018-09-08 00:00:00')
# x2 = pd.to_datetime('20190902',format='%Y%m%d')
# #Timestamp('2019-09-01 00:00:00')
# print(x2)
#
# from dateutil.parser import parse
#
# a=20170825113215
# b=str(a)
# c=parse(b)
# print(c)


