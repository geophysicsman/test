from matplotlib import pyplot as plt
import numpy as np
#导入3d包
from mpl_toolkits.mplot3d import Axes3D
# 创建X,Y,Z
X=[1,2,2,2,1,2,2,1]
Y=[3,6,4,3,5,2,4,3]
Z=[1,10,17,1,23,14,16,8]
figure=plt.figure()
# 创建Axes3D对象
ax=Axes3D(figure)
ax.plot_trisurf(X,Y,Z)
plt.show()