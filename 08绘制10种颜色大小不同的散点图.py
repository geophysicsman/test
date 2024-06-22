from matplotlib import pyplot as plt
import numpy as np

# 绘制10种大小、100种颜色不同的散点图
# 创建x
np.random.seed(0) # 执行多次每次获取的随机数是一样的
x=np.random.rand(100)
y=np.random.rand(100)
# 生成10种大小
size=np.random.rand(100)*1000
# 生成100种颜色
color=np.random.rand(100)
print(x)
print(y)
# 绘制散点图
plt.scatter(x,y,s=size,c=color,alpha=0.7) # s表示点的大小 c表示颜色 alpha表示透明度
plt.show()
plt.savefig('sandiantu.jpg')

'''
注意：点的个数和颜色的个数要相同
      点的个数和点的大小的个数可以不同,如果点的个数大于大小的个数，则会循环获取大小
'''