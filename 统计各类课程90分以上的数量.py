import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
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
kind1 = '前端开发'
kind2 = '后端开发'
kind3 = '数据库'
kind4 = '运维&测试'
kind5 = '移动开发'
kind6 = 'UI设计&多媒体'
kind7 = '云计算&大数据'
kind8 = '游戏'
a = [0 for x in range(0, 16)]
print()
for i in range(len(column[0])):
    if column[1][i] == kind1:
        if 100 >= eval(column[3][i]) >= 95:
            a[0] = a[0]+1
        if 95 > eval(column[3][i]) >= 90:
            a[1] = a[1]+1
    if column[1][i] == kind2:
        if 100 >= eval(column[3][i]) >= 95:
            a[2] = a[2]+1
        if 95 > eval(column[3][i]) >= 90:
            a[3] = a[3]+1
    if column[1][i] == kind3:
        if 100 >= eval(column[3][i]) >= 95:
            a[4] = a[4]+1
        if 95 > eval(column[3][i]) >= 90:
            a[5] = a[5]+1
    if column[1][i] == kind4:
        if 100 >= eval(column[3][i]) >= 95:
            a[6] = a[6]+1
        if 95 > eval(column[3][i]) >= 90:
            a[7] = a[7]+1
    if column[1][i] == kind5:
        if 100 >= eval(column[3][i]) >= 95:
            a[8] = a[8]+1
        if 95 > eval(column[3][i]) >= 90:
            a[9] = a[9]+1
    if column[1][i] == kind6:
        if 100 >= eval(column[3][i]) >= 95:
            a[10] = a[10]+1
        if 95 > eval(column[3][i]) >= 90:
            a[11] = a[11]+1
    if column[1][i] == kind7:
        if 100 >= eval(column[3][i]) >= 95:
            a[12] = a[12]+1
        if 95 > eval(column[3][i]) >= 90:
            a[13] = a[13]+1
    if column[1][i] == kind8:
        if 100 >= eval(column[3][i]) >= 95:
            a[14] = a[14]+1
        if 95 > eval(column[3][i]) >= 90:
            a[15] = a[15]+1
custom_font = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')

font_size = 10 # 字体大小
fig_size = (20, 20) # 图表大小

names = (u'前端开发', u'后端开发', u'数据库', '运维&测试', '移动开发', 'UI设计&多媒体', '云计算&大数据', '游戏' ) # 分类
subjects = ('100-90', '94-90') # 评分
scores = ((a[0], a[1]), (a[2], a[3]), (a[4], a[5]), (a[6], a[7]), (a[8], a[9]), (a[10], a[11]), (a[12], a[13]), (a[14], a[15])) # 成绩

# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size
# 设置柱形图宽度
bar_width = 0.1

index = np.arange(len(scores[0]))
# 绘制「kind1」
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
# 绘制「kind2」的成绩
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
rects3 = plt.bar(index+ 2*bar_width, scores[2], bar_width, color='#1E90FF', label=names[2])
rects4 = plt.bar(index+ 3*bar_width, scores[3], bar_width, color='#00BFFF', label=names[3])
rects5 = plt.bar(index+ 4*bar_width, scores[4], bar_width, color='#008000', label=names[4])
rects6 = plt.bar(index+ 5*bar_width, scores[5], bar_width, color='#FFA500', label=names[5])
rects7 = plt.bar(index+ 6*bar_width, scores[6], bar_width, color='#A0522D', label=names[6])
rects8 = plt.bar(index+ 7*bar_width, scores[7], bar_width, color='#800000', label=names[7])
# X轴标题
plt.xticks(index + bar_width, subjects, fontproperties=custom_font)
# Y轴范围
plt.ylim(ymax=300, ymin=0)
# 图表标题
plt.title(u'90分以上不同种类课程的数量', fontproperties=custom_font)
# 图例显示在图表下方
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5, prop=custom_font)

# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
add_labels(rects4)
add_labels(rects5)
add_labels(rects6)
add_labels(rects7)
add_labels(rects8)
# 图表输出到本地
plt.savefig('scores_par.png')