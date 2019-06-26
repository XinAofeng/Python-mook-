import sys
import bs4
from urllib import request

from bs4 import BeautifulSoup


def GetHtmlContext(url):
    try:
        f = request.urlopen(url)
        data = f.read()
        return data
    except:
        return 0


def GetData(html, url):

    data = []
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('div', attrs={'class': 'hd clearfix'})
    if isinstance(title, bs4.element.Tag):
        data.append(title.find('h2', attrs={'class': 'l'}).getText())
    lesson = soup.find('div', attrs={'class': 'statics clearfix'})
    if isinstance(lesson, bs4.element.Tag):
     for attr in lesson.find_all('div', attrs={'class': 'static-item l'}):
        data.append(attr.find('span', attrs={'class': 'meta-value'}).getText())
    if isinstance(lesson, bs4.element.Tag):
        grade = lesson.find('div', attrs={'class': 'static-item l score-btn'})
        data.append(grade.find('span', attrs={'class': 'meta-value'}).getText())
        data.append(url)
        data.remove('')
        print(outputMode.format(data[0], data[1], data[2], data[3], data[4], chr(12288)))


# 将输出重定向到txt文件
output = sys.stdout
outputfile = open(r"C:\Users\10713\Desktop\fxa.txt", 'w', encoding='utf-8')
sys.stdout = outputfile


outputMode = "{0:{5}^20}\t{1:^10}\t{2:^10}\t{3:^10}\t{4:{5}<10}"
print(outputMode.format('课程名称', '难度', '课程时长', '综合评分', '课程链接', chr(12288)))
baseUrl = "http://www.imooc.com/learn/"
k = 0
while k < 1000:
    url = baseUrl + str(k)
    html = GetHtmlContext(url)
    k += 1
    if(html != 0):
        GetData(html, url)

outputfile.close()
sys.stdout = output