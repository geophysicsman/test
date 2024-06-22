from matplotlib import pyplot as plt
import numpy as np
# 生成0-10之间的100个等差数
x=np.linspace(0,10,100)
# 进行绘制正弦和余弦曲线
sin_y=np.sin(x)
plt.plot(x,sin_y)
cos_y=np.cos(x)
plt.plot(x,cos_y)
# 保存图片
plt.savefig('sin_cos.jpg')
plt.show()