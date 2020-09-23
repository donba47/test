# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:03:43 2020

@author: petertw89
"""
# -*-coding: UTF-8 -*-
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


system = signal.lti([1], [1.44*10**-4,1])		# RC的Transfer function(s Domain)，1.44*10**-4為R*C
f = np.logspace(0,6)								# X軸取對數成長10^0Hz ~ 10^6Hz
w = 2 * np.pi * f									# 角頻率
w, mag, phase = signal.bode(system, w)         # 計算, mag=增益關係，phase=相位關係    
plt.figure(figsize=(10,10),dpi=250)         #設定子圖配置
plt.subplot(211)			#子圖一
plt.subplots_adjust(wspace=0,hspace =0.35)#子圖一參數
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.semilogx(f, phase)                          # 繪製頻率-增益曲線
plt.scatter(6.944*(10**3)/(2*np.pi),-45)        #標點(截止頻率)
plt.title("Bode Diagram",  #標題
           fontweight = "bold",fontsize=16) 		
plt.ylabel("Phase(deg)", fontweight = "bold",fontsize=12) #y座標
plt.hlines(-45,0,10**3,linestyle= '--',colors = "r")    #畫水平線(y,xstart,xend)
plt.vlines(6.944*(10**3)/(2*np.pi),-90,-45,linestyle= '--',colors = "r")   #畫垂直線(x,ystart,yend)                 	
plt.annotate(r'Cutoff frequency=1.105KHz',              #圖上註解
         xy=(6.944*(10**3)/(2*np.pi),-45), xycoords='data', xytext=(+15, -15),c="b",
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.annotate(r'at Phase=45 degree',
         xy=(6.944*(10**3)/(2*np.pi),-45), xycoords='data', xytext=(+30, -30),c="b",
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.xlabel("Frequency(Hz)", fontweight = "bold",fontsize=12)#y軸
plt.xlim(1,) #X軸顯示範圍
plt.ylim(-92,)#Y軸顯示範圍
plt.subplot(212)			#子圖2
plt.semilogx(w,mag)                 # 繪製頻率-相位曲線
plt.scatter(6.944*(10**3),-3)           #標點(截止頻率)
plt.ylabel("Magnitude(dB)", fontweight = "bold",fontsize=12)        #y座標
plt.xlabel("Frequency(rad/s)", fontweight = "bold",fontsize=12)     #X座標
plt.hlines(-3,1*2*np.pi,6.944*(10**3),linestyle= '--',colors = "r") #畫水平線(y,xstart,xend)
plt.vlines(6.944*(10**3),-60,-3,linestyle= '--',colors = "r")       #畫垂直線(x,ystart,yend)             	
plt.annotate(r'         Cutoff frequency($\omega_0$)=6.944*10^3 (rad/s)',#圖上註解
         xy=(6.944*(10**3),-3), xycoords='data', xytext=(+15, -15),c="b",
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.annotate(r'         at Magnitude=-3 dB',                        #圖上註解
         xy=(6.944*(10**3),-3), xycoords='data', xytext=(+30, -30),c="b",
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.xlim(1*2*np.pi,) #X軸顯示範圍
plt.ylim(-60,)#Y軸顯示範圍
plt.savefig("Bode Diagram") #存檔名稱
plt.show()#顯示圖片
plt.close() 										

