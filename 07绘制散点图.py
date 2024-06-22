from matplotlib import pyplot as plt
import numpy as np
# 创建0-10之间的100个等差数
x=np.linspace(1,10,100)
sin_y=np.sin(x)
# # 绘制正弦曲线
plt.plot(x,sin_y,'s')
# plt.plot(x,sin_y)
# # 绘制散点图
# plt.scatter(x,sin_y)
plt.show()

'''
从上面的实例可以看到，使用plot绘制和使用scatter绘制出来的图形是没有区别的，
但是使用Plot绘制图形的速度由于scatter，如果画一堆点，而且点的形式没有差别，
那么我们使用plot,如果点的形式有差别（指点的大小、颜色不同）则必须使用scatter
'''