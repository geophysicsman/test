import matplotlib.pyplot as plt
import numpy as np

# 准备数据
# 三部电影的名称
real_names=['千与千寻','玩具总动员4','黑衣人']
# 三天内票房数
real_num1=[7548,4013,1673]
real_num2=[5453,1840,1080]
real_num3=[4348,2345,1890]
x=np.arange(len(real_names))
# 绘制柱状图
width=0.3
plt.bar(x,real_num1,alpha=0.5,width=width,label=real_names[0])
plt.bar([i+width for i in x],real_num2,alpha=0.5,width=width,label=real_names[1])
plt.bar([i+2*width for i in x],real_num3,alpha=0.5,width=width,label=real_names[2])
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
# 设置x坐标的值 第一天 第二天 第三天
x_label=['第{}天'.format(i+1) for i in x]
plt.xticks([i+width for i in x],x_label)
# 添加y坐标的值
plt.ylabel('票房数')
# 添加图例
plt.legend()
# 添加标题
plt.title('三天三部电影播放量')
plt.show()
