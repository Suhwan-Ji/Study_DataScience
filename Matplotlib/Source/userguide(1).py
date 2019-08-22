import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle('No axes on thos figure')
print(fig)
fig, ax_list = plt.subplots(2,2) #2x2 축 추가
print(fig)
print(ax_list)

'''
axes : 서브플롯객체
axis : 축, tick의 위치는 Locater , tick라벨은 Formmatter객체로 정해짐
artist : 플롯상에 보이는 모든것, 대부분 하나의 Axes에 묶여 있음
'''

#입력 : np.array 입력을 받음
#판다스같은 객체는 원하는대로 동작안할수도 있으므로 변환하고 넣는것이 좋음
import pandas as pd
a = pd.DataFrame(np.random.rand(4,5),columns = list('abcde'))
print(a)
a_asarray = a.values
print(a_asarray)
print('-------------')
b = np.matrix([[1,2],[3,4]])
print(b)
b_asarray = np.asarray(b)
print(b)

#pyplot은 전체 matplotlib의 모듈임
#pyplot의 함수는 항상 '현재'그림이 있음
#plt.plot은 axes를 만들고 plt.plt를 한번더 하면 같은 곳에 그림을 그림
x = np.linspace(0,2,100)

plt.plot(x,x,label = 'linear')
plt.plot(x,x**2,label = 'quadratic')
plt.plot(x,x**3,label = 'cubic')

plt.xlabel('x label')
plt.xlabel('y label')

plt.title('Simple plot')
plt.legend()
plt.show()