import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.font_manager import FontProperties
file = open(r'C:\Users\10713\Desktop\python作业\Python-mook-\data.csv', mode='r')
lines = file.readlines()
file.close()
row=[]
column=[]
for line in lines:
    row.append(line.split(','))
for col in row:
       column.append(col)
num1=num2=num3=num4=0#用以统计各种难度的数量
level1='入门'
level2='初级'
level3='中级'
level4='高级'
for i in column[2]:
    if i == level1:
        num1= num1+1
    if i == level2:
        num2 = num2+1
    if i == level3:
        num3 = num3+1
    if i == level4:
        num4 = num4+1
print(num1)
print(num2)
print(num3)
print(num4)
plt.figure(figsize=(8, 6), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)
# 柱子总数
N = 4
# 包含每个柱子对应值的序列
values = (num1, num2, num3, num4)
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="number", color="#FFA500")
# 设置横轴标签
plt.xlabel('level')
# 设置纵轴标签
plt.ylabel('number ')
# 添加标题
plt.title('The Number of Each Level ')
# 添加纵横轴的刻度
plt.xticks(index, ('introduction', 'primary', 'intermidiate', 'adanced'))
plt.yticks(np.arange(0, 400, 20))
# 添加图例
for i in p2:
    height = i.get_height()
    plt.text(i.get_x()+i.get_width()/2, height+1, str(height), ha="center", va="bottom")
plt.show()



