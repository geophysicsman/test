#coding=utf-8
# 导入模块
import matplotlib.pyplot as plt
# 准备x,y
x=[1,2,3,4,5]
y=[1,4,9,16,25]
# 绘制折线
# linewidth属性设置线条宽度
plt.plot(x,y,linewidth=3)
# 添加x和y轴名称
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
# 给图片添加标题
plt.title('折线图')
plt.show()

