from qqbot import _bot as bot
import requests
from lxml import etree
import time
bot.Login(['-q', '2694010411']) #登陆一下
sent_list=['1120897575','411774285','1961346989','1466648053','2621564050','1244979861','378853264']
def film_name(a):
    s_words = etree.HTML(a)
    for num_list in range(25):
        num_list += 1
        cn_name = s_words.xpath('//*[@id="content"]/div/div[1]/ol/li[' + str(num_list) + ']/div/div[2]/div[1]/a/span[1]/text()') # 电影名
        words = s_words.xpath('//*[@id="content"]/div/div[1]/ol/li[' +str(num_list) + ']/div/div[2]/div[2]/p[2]/span/text()')  # 一句话
        str_name_not=str(cn_name) #同下
        str_name_yes=str_name_not[2:-2] #参考下面
        str_words_not=str(words) #转换类型
        str_words_yes=str_words_not[2:-2] #去掉多余的东西
        str_sent=str_name_yes+'——'+str_words_yes #拼接字符串
        for qqfriend in sent_list:
            bl = bot.List('buddy',qqfriend) #发送给谁
            if bl:                          #不知道在这里判断了什么 (－‸ლ)无语
                b = bl[0]
                bot.SendTo(b,str_sent)
        time.sleep(5400) #休眠，三小时发送一次   休眠到底加在哪里！！！！！


def douban_listdef():
    for list_num in range(0, 250, 25):
        douban_page = requests.get('https://movie.douban.com/top250?start=' + str(list_num)).text
        film_name(douban_page)

douban_listdef()

#没有实现。。。。再想一想.....


