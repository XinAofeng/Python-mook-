import matplotlib.pyplot as plt
import numpy as np
import string
file = open(r'C:\Users\10713\Desktop\python作业\Python-mook-\data.csv', mode='r')
lines = file.readlines()
file.close()
row=[]
column=[]
for line in lines:
    row.append(line.split(','))
for col in row:
       column.append(col)
globals = {
    'nan': 0
}
num1 = num2 = num3 = num4 = num5 = num6 = num7 = num8 = 0
kind1 = '前端开发'
kind2 = '后端开发'
kind3 = '数据库'
kind4 = '运维&测试'
kind5 = '移动开发'
kind6 = 'UI设计&多媒体'
kind7 = '云计算&大数据'
kind8 = '游戏'
for i in column[1]:
    if i == kind1:
        num1 = num1 + 1
    if i == kind2:
        num2 = num2 + 1
    if i == kind3:
        num3 = num3 + 1
    if i == kind4:
        num4 = num4 + 1
    if i == kind5:
        num5 = num5 + 1
    if i == kind6:
        num6 = num6 + 1
    if i == kind7:
        num7 = num7 + 1
    if i == kind8:
        num8 = num8 + 1
plt.figure(figsize=(14, 10), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)
# 柱子总数
N = 8
# 包含每个柱子对应值的序列
values = (num1, num2, num3, num4, num5, num6, num7, num8)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.25
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="number", color="#87CEFA")
# 设置横轴标签
plt.xlabel('kinds')
# 设置纵轴标签
plt.ylabel('number (1)')
# 添加标题
plt.title('The Number of Each kinds of courses')
# 添加纵横轴的刻度
plt.xticks(index, ('front-end development', 'backend development', 'database', 'operation', 'mobile development','multimedia', 'cloud computing', 'game'))
plt.yticks(np.arange(0, 300, 10))
# 添加图例
for i in p2:
    height = i.get_height()
    plt.text(i.get_x()+i.get_width()/2, height+1, str(height), ha="center",va="bottom" )
plt.savefig('种类为横坐标的柱状图.png')
labels = 'front-end development', 'backend development', 'database', 'operation', 'mobile development','multimedia', 'cloud computing', 'game'
fracs = [num1, num2, num3, num4, num5, num6, num7, num8]
explode = [0, 0.1, 0, 0, 0, 0, 0, 0]  # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
# autopct ，show percet
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6

        )
plt.savefig('种类为横坐标饼状图.png')