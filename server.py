# -*- coding:utf-8 -*-
import os
import time
from selenium import webdriver
import re
import urllib.request
import sys
"""
获取js加载后的html
"""
def getHtml(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def open_url(url):
    # 根据当前URL创建请求包
    req = urllib.request.Request(url)
    # 添加头信息，伪装成浏览器访问
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    response = urllib.request.urlopen(req)
    return response.read()


"""
获取html中的img图片
"""
def downImg(html, url) :
    imgRes = re.findall(r'<img src="(.*?)"', html)
    urlHander = re.findall(r'htt[a-z]+://.*?/', url)
    if not urlHander:
        urlHander = url
    else:
        urlHander = urlHander[0]
    for img in imgRes:
        if img.find('http') == -1:
            img = urlHander + img
        if not re.findall(r'\.png|\.jpg|\.bpm|\.gif|\.svg', img):
            continue
        print('download image:%s' % img)
        filename = img.split('?')[0]
        filename = str(filename).split('/')[-1]
        with open(filename, 'wb') as f:
            # 返回请求到的HTML信息
            url = open_url(img)
            # 下载图片
            f.write(url)
"""
    `url`  指定url 
    `cdnHttp`  指定图片cdn, 只填写前面部分 如:http://cdn.***.com
    `fileName`  保存文件名称可为空
"""
def downloadImg(url, fileName=''):
    if url == False:
        return
    os.chdir(sys.path[0])
    if not fileName:
        fileName = 'download' + str(time.time())
    # 判断文件夹不存在就创建文件夹
    if not os.path.exists(fileName):
        os.mkdir(fileName)
    # 将脚本的工作环境移动到创建的文件夹下
    os.chdir(fileName)
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        html = driver.page_source  # 把页面打印出来
        downImg(html, url)
        driver.quit()
        return True
    except:
        driver.quit()
        return False

