import matplotlib .pyplot as plt
import numpy as np
# 创建x
x=np.linspace(0,10,100)
# 使用legend()图例，给plot方法添加参数label
plt.plot(x,x+0,'--g',label='--g')
plt.plot(x,x+1,'-.r',label='-.r')
plt.plot(x,x+2,':',label=':')
plt.plot(x,x+3,'.k',label='.k')
plt.plot(x,x+4,',c',label=',c')
plt.plot(x,x+5,'*y',label='*y')
# 左上角upper left fancybox边框 framealpha透明度 shadow阴影 borderpad边框宽度
plt.legend(loc='upper left',fancybox=True,
           framealpha=0.5,shadow=True,boardpad=1) # 默认的位置再左上角upper left 可以通过loc修改
plt.show()