#-*- coding:utf-8 -*-
import requests
from lxml import etree
from bs4 import BeautifulSoup
import openpyxl
#——————————————————分割线————————————————————————————————————————————————————————————————————————————————————————————
id=input("请输入学号:")
s = requests.Session()
s.get('https://www.shzurk.com/ThinkYibanclass/index.php/Main/index?username=loner&studentid='+id+'&teacherid=')
r = s.get("https://www.shzurk.com/ThinkYibanclass/index.php/Main/myClass").text
#print(r.text)

#r=requests.get(url).text
data = BeautifulSoup(r,'lxml')
class_name=data.select("div.major > p.kcmc")
class_week=data.select("div.major > p.skzs")
class_time=data.select("div.major > p.jc")
class_xq=data.select("div.major > p.xq")
class_place=data.select("div.major > p.dd")
class_name_del=[]
class_week_del=[]
class_time_del=[]
class_xq_del=[]
class_place_del=[]
def del_data(list_name,out_data):
    for data in list_name:
        text=data.get_text()
        out_data.append(text)
del_data(class_name,class_name_del)
del_data(class_week,class_week_del)
del_data(class_time,class_time_del)
del_data(class_xq,class_xq_del)
del_data(class_place,class_place_del)
xq=[]
week=[]
excel_list=[["name", "type", "time", "during","teacher","place"]]
for a in class_xq_del:
    xq.append(a.replace('星期', '周'))
for w in class_week_del:
    week.append(w.replace(',','周&')+'周')

n=0
for n in range(0,len(class_name_del)):
    class_list=[class_name_del[n],"type",str(xq[n])+" "+str(class_time_del[n])+"节",week[n],"teacher",class_place_del[n]]
    n=n+1
    excel_list.append(class_list)
#print(excel_list)

#下面是写出到excell
def write07Excel():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'KB'
    for i in range(0, len(class_name_del)):
        for j in range(0, len(excel_list[i])):
            sheet.cell(row=i+1, column=j+1, value=str(excel_list[i][j]))
    wb.save(id + ".xlsx")
    print("课程表导出成功！")
write07Excel() #启动
