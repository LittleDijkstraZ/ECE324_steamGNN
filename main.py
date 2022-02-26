import urllib.request, urllib.error   #制定url，获取网页数据
import re       #正则表达式，文字匹配
from bs4 import BeautifulSoup     #网页解析
import xlwt     #excel操作
import sqlite3  #数据库操作

def main():
    baseurl = "https://steamdb.info/instantsearch/"

    # 提取数据
    datalist = getData(baseurl)

    # 保存数据
    save_path = "./steamWorkSheet"
    saveData(save_path)


def getData(url):
    datalist = []
    return datalist

def saveData(path):
    pass