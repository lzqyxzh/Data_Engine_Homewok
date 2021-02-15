# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 02:22:03 2021

@author: hp
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

    # 得到页面的内容
def get_page_content(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    print(url)
    html = requests.get(url,headers = headers,timeout = 10)
    content = html.text
    soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')
    return soup
    
# 分析当前页面的投诉信息
def analysis(soup):
    df = pd.DataFrame(columns=['id','brand','car_model','car_type','problem_desc','problem','data','status'])
    # 找到完整的投诉信息框
    temp = soup.find('div',class_='tslb_b')
    # 找出所有的tr，即行
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        # 如果没有td，就是表头，这个网页里就是 th
        if len(td_list) > 0:          #td_list的长度＞0，则说明这个tr不是表头，可以进行数据的爬取
            # 投诉编号	投诉品牌	投诉车系	投诉车型	问题简述	典型问题	投诉时间	投诉状态
            id,brand,car_model,car_type,problem_desc,problem,data,status = td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            # 设置一个字典存放爬取的字段
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model']=car_model
            temp['car_type']=car_type
            temp['problem_desc']=problem_desc
            temp['problem']=problem
            temp['data']=data
            temp['status']=status
            # 将字典的内容append到DataFrame中
            df = df.append(temp,ignore_index=True)
    return df

# 请求url
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-1_0-2-0-0-0-0-0-'
# 要爬取的页数
page_num = 20
# 构建存放最终20页结果的result
result=pd.DataFrame(columns=['id','brand','car_model','car_type','problem_desc','problem','data','status'])

for i in range(page_num):
    url = base_url + str(i+1) + '.shtml'
    soup = get_page_content(url)
    df = analysis(soup)
    result = result.append(df)

result = result.reset_index(drop=True) #重置索引
result.to_excel('车质网汽车投诉数据表.xlsx')
print('爬取数据完成，数据已保存至当前文件夹下的《车质网汽车投诉数据表》表格中')