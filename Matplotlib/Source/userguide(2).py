#Coding Styles
#여러 방법이 있지만 섞어 쓰지는 말고, 권장하는 방법은 두가지임

# 1) Pyplot Style , 맬랩스타일?
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.2)
y= np.sin(x)
fig, ax = plt.subplots()
print(dir(fig),'\n--------------------\n',dir(ax))
ax.plot(x,y)
plt.show()

# 2) wordier style?? 어디객체인지 훨씬 명확해서 어플리케이션이 복잡할수록 강력함
#같은 그래프에 여러개를 그리려면 함수를 작성하는것이 편함

def myplotter(ax,data1,data2,param_dict):
    out = ax.plot(data1,data2,**param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4,100)
fig, ax = plt.subplots(1,1)
myplotter(ax,data1,data2,{'marker':'x'})

#fig, (ax2,ax3) = plt.subplots(1,2)
#myplotter(ax2,data1,data2,{'marker':'x'})
#myplotter(ax3,data3,data4,{'marker':'o'})

fig, ax_list = plt.subplots(1,2)
myplotter(ax_list[0],data1,data2,{'marker':'x'})
myplotter(ax_list[1],data3,data4,{'marker':'o'})

plt.show()
#지금은 오바같지만 나중에 더욱더 복잡해질수록 이 방식이 좋음??