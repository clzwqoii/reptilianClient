# -*- coding: UTF-8 -*-
from tkinter import *           # 导入 Tkinter 库
import tkinter.messagebox           # 导入 Tkinter 库
import server
def getImg(button):
    url = inputUrlTitle.get()
    res = server.downloadImg(url)
    if res:
        tkinter.messagebox.askokcancel(title='成功', message='数据获取很成功')
    else:
        tkinter.messagebox.askokcancel(title='警告', message='数据获取出现问题, 不完整 !')

root = Tk()                     # 创建窗口对象的背景色
root.title("爬图小公具--小小殇")
root.geometry('700x500')
root.resizable(width=False, height=True)
 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
frame = Frame(height = 10000,width = 10000,bg = '#444')
Label(frame, text="本工具用于抓取指定网站的图片！", bg="#444", font=("Arial", 16), width=100, height=2).pack()
inputUrlTitle = StringVar()
inputUrlTitle.set('请输入完整网址, 如:https://baidu.com')
Label(frame, text="请输入url", background = '#444').pack()
text = Entry(frame, background='#444',width=50, textvariable=inputUrlTitle).pack()
Label(frame, text="请输入保存图片的文件名称(非必填)", background = '#444').pack()
Entry(frame, background = '#444',width=50).pack()
Label(frame, text="", height=1, width=10,background = '#444').pack()
button = Button(frame, text="提交", bg='#2d78f4', command=lambda:getImg(button), border='1px solid #2d78f4',width=15, height=1).pack()
Label(frame, text='', width=100, height=200, bg='#444', ).pack()
frame.pack()
root.mainloop()                 # 进入消息循环
