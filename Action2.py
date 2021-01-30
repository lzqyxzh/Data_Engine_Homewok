# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:44:04 2021

@author: hp
"""

import pandas as pd

# path=r'E:\LiuZhiqiang\onedrive\OneDrive - 上汽大众汽车有限公司\Work Document\python\数据黑马\L1\car_data_analyze\Action2.xlsx'
data=pd.read_excel('Action2.xlsx')
aver_yuwen = data['语文'].mean()
max_yuwen = data['语文'].max()
min_yuwen = data['语文'].min()
max_yuwen_name = data['姓名'][data['语文'].idxmax()]
min_yuwen_name = data['姓名'][data['语文'].idxmin()]
std_yuwen=data['语文'].std() #标准差
var_yuwen=std_yuwen**2 #方差

aver_shuxue = data['数学'].mean()
max_shuxue = data['数学'].max()
min_shuxue = data['数学'].min()
max_shuxue_name = data['姓名'][data['数学'].idxmax()]
min_shuxue_name = data['姓名'][data['数学'].idxmin()]
std_shuxue=data['数学'].std() #标准差
var_shuxue=std_shuxue**2 #方差


aver_yingyu = data['英语'].mean()
max_yingyu = data['英语'].max()
min_yingyu = data['英语'].min()
max_yingyu_name = data['姓名'][data['英语'].idxmax()]
min_yingyu_name = data['姓名'][data['英语'].idxmin()]
std_yingyu=data['英语'].std() #标准差
var_yingyu=std_yingyu**2 #方差

print('语文平均分是{}分，最高分是{}的{}分，最低分是{}的{}分，方差是{:.2f},标准差是{:.2f}'.format(aver_yuwen,max_yuwen_name,max_yuwen,min_yuwen_name,min_yuwen,var_yuwen,std_yuwen))
print('数学平均分是{}分，最高分是{}的{}分，最低分是{}的{}分，方差是{:.2f},标准差是{:.2f}'.format(aver_shuxue,max_shuxue_name,max_shuxue,min_shuxue_name,min_shuxue,var_shuxue,std_shuxue))
print('英语平均分是{}分，最高分是{}的{}分，最低分是{}的{}分，方差是{:.2f},标准差是{:.2f}'.format(aver_yingyu,max_yingyu_name,max_yingyu,min_yingyu_name,min_yingyu,var_yingyu,std_yingyu))

data['总分']=data.sum(axis=1)
data.sort_values(by='总分',ascending=False,inplace=True)
data.reset_index(drop=True,inplace=True)
print('\n总分排名如下：')
print(data)
