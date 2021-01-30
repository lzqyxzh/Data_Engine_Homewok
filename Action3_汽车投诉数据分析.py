# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:24:29 2021

@author: hp
"""

import pandas as pd
import collections
pd.options.mode.chained_assignment = None #设置pandas不显示Warning信息

# path=r'E:\LiuZhiqiang\onedrive\OneDrive - 上汽大众汽车有限公司\Work Document\python\数据黑马\L1\car_data_analyze\car_complain.csv'
# 拆分problem字段
data=pd.read_csv('car_complain.csv')
for i in range(len(data)):
    problem_list = data['problem'][i].split(',')
    problem_list.pop()
    for problem in problem_list:
        data.loc[i,problem]=1
data=data.fillna(0)

# 将‘一汽大众’改为‘一汽-大众’
for j in range(len(data)):
    if data['brand'][j] == '一汽大众':
        data['brand'][j] = '一汽-大众' #这一句会出现Warning
    else:
        continue

# 统计品牌投诉量
data_group_brand=data.groupby('brand').size()
data_group_brand.sort_values(ascending=False,inplace=True)
print('\n1. 投诉量最多的品牌是：{}，共有{}个投诉'.format(data_group_brand.index[0],data_group_brand[0]))


# 统计车型投诉量
data_group_car= data.groupby('car_model').size()
data_group_car.sort_values(ascending=False,inplace=True)
print('2. 投诉量最多的车型是：{}，共有{}个投诉'.format(data_group_car.index[0],data_group_car[0]))

# 计算品牌内车型投诉情况

brand=[]
data_group= data.groupby(['brand','car_model']).size()
for x in range(len(data_group)):
    brand.append(data_group.index[x][0])
brand = pd.Series(brand)
brand_count = brand.value_counts()
a=brand_count.sort_index()
b=data_group_brand.sort_index()
c=b/a
c.sort_values(ascending=False,inplace=True)
print('3. {} 的车型平均投诉最多，每种车型平均收到{}个投诉，其共有{}个车型，总投诉量是{}个\n'.format(c.index[0],c[0],a[c.index[0]],b[c.index[0]]))


