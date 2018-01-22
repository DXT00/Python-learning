# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup   #用于解析HTML
import os
__author__ = 'DXT- '


for i in range(2,10):#爬取第2到第10页

    #打开首页
    response= request.urlopen('https://desk.zol.com.cn/dongwu/%s.html' %i)
    html=response.read()#返回了网页的HTML源代码！
    # print(response.read())#返回了网页的源代码！

    #解析图片集的url和title组成一个数据列表
    soup=BeautifulSoup(html,'html.parser',from_encoding='gbk')#根据返回的HTML文件写编码--> content="text/html; charset=gb2312-->返回的是二进制（b)
    #获取所有的图片li
    lis=soup.find_all('li',class_='photo-list-padding')#print(lis)

    #数据列表
    info_list=[]
    for li in lis:
        temp={}
        a=li.find_all('a')[0]
        #返回的是一个所有a标签的列表-->所以加[0]-->即找到每个li的第一个a标签
        img=li.find_all('img')[0]
        #与a标签同理
        temp['url']="https://desk.zol.com.cn%s"%a['href']
        temp['title']=img['alt']
        info_list.append(temp)

    #print(len(info_list))
    #循环数据表
    for info in info_list:
        print(info)
        bigimg_list = [] #获取大图列表


        response1=request.urlopen(info['url'])#每一条数据的url发送请求
        htm = response1.read()

        soup1 = BeautifulSoup(htm,'html.parser',from_encoding='gbk') #解析，获取大图列表
        imgres=soup1.find_all('img',id="bigImg")[0]['src']
        # bigimg_list.append(imgres)
        #print(imgres)


        ul = soup1.find_all('ul',id="showImg")[0]
        img_lis = ul.find_all('li')  #list列表-->10张图片列表


        for li in img_lis:
            img_a =li.find_all('a')[0]

            sub_url="https://desk.zol.com.cn%s"%img_a['href']
            print(sub_url)
            response2=request.urlopen(sub_url)#每一条数据的sub_url发送请求
            html3 = response2.read()
            soup2 = BeautifulSoup(html3,'html.parser',from_encoding='gbk') #解析，获取大图列表
            sub_imgres=soup2.find_all('img',id="bigImg")[0]['src']
            bigimg_list.append(sub_imgres)

        print(bigimg_list)

        #新建一个文件夹
        os.mkdir(info['title'])
        #循环下载图片
        j = 1
        for url in bigimg_list:
            #获取图片二进制信息
            img_data = request.urlopen(url).read()
            with open('%s\\%s.jpg'%(info['title'],j),'wb') as f:
                f.write(img_data)
            j += 1


