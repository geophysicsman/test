import matplotlib.pyplot as plt
import numpy as np
# 生成x,y
np.random.seed(0)
x=np.arange(5)
y=np.random.randint(-5,5,5)

# 添加颜色
v_bar=plt.bar(x,y,color='blue')

# 对y值大于0的设置蓝色 小于0的柱设置绿色
for bar,height in zip(v_bar,y):
    if height<-2:
        bar.set(color='green')
    elif height>0:
        bar.set(color='red')
plt.show()