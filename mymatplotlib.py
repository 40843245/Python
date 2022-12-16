import matplotlib.pyplot as plt

xpt = [1,3,5]
ypt = [1,9,25]
plt.plot(xpt,ypt) #畫線
plt.xticks([0,5,10]) #設定x軸刻度
plt.yticks([0,10,20,50]) #設定y軸刻度
plt.tick_params(axis='both', labelsize=60, color='green')
plt.show() #顯示繪製的圖形