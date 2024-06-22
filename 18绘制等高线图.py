from matplotlib import pyplot as plt
import numpy as np

G=6.67* 10**(-11)
D=100
sigma=1000
R=50
pi=3.1415926
M=(4/3)*pi*sigma*(R**3)
# 创建x,y
x=np.linspace(-200,200,180)
y=np.linspace(-200,200,180)
# 计算x,y相交的点X Y
X,Y=np.meshgrid(x,y)
# 计算Z
#Z=np.sqrt(X**2+Y**2)
Z=(G*M*D)/((X**2+Y**2+D**2)**1.5)
# 绘制等高
plt.contour(X,Y,Z)
#plt.contourf(X,Y,Z)# 填充空白
plt.show()
