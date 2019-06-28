import matplotlib.pyplot as plt
import numpy as np

file = open(r'C:\Users\10713\Desktop\python作业\Python-mook-\data.csv', mode='r')
lines = file.readlines()
file.close()
row=[]
column=[]
for line in lines:
    row.append(line.split(','))
for col in row:
       column.append(col)
print(column[4][4])#column类似于二维数组，行标为行，列表为列，从0开始
num1 = num2 = num3 = num4 = 0
for i in column[3]:
    if 100 >= eval(i)>=96:
        num1 = num1+1
    if  95>=eval(i)>=91:
        num2 =num2+1
    if  90>=eval(i)>=86:
        num3=num3+1
    if  85>=eval(i)>=80:
        num4=num4+1
print(num1)
print(num2)
print(num3)
print(num4)
#for i in column[3]:
 #  if 85 >= row.count(i) >= 80:
  #    num1 = num1+1
#统计数据，以评分为标准，各类课程为不同颜色的柱状，高度为数量
# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
#80-85,86-90,91-95,96-100,分为4组
print(num1)
plt.figure(figsize=(8, 6), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)
# 柱子总数
N = 4
# 包含每个柱子对应值的序列
values = (num4, num3, num2, num1)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="number", color="#87CEFA")
# 设置横轴标签
plt.xlabel('range(1)')
# 设置纵轴标签
plt.ylabel('number (1)')
# 添加标题
plt.title('The Number of Each Level ')
# 添加纵横轴的刻度
plt.xticks(index, ('80-85', '86-90', '91-95', '96-100'))
plt.yticks(np.arange(0, 500, 20))
# 添加图例
for i in p2:
    height = i.get_height()
    plt.text(i.get_x()+i.get_width()/2, height+1, str(height), ha="center",va="bottom" )
plt.show()