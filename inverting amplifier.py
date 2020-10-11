# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 07:58:20 2020

@author: petertw89
"""
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


system = signal.lti([-10], [1/571198.664,1])		# RC的Transfer function(s Domain)，1.44*10**-4為R*C
f = np.logspace(0,8)								# X軸取對數成長10^0Hz ~ 10^6Hz
w = 2 * np.pi * f									# 角頻率
w, mag, phase = signal.bode(system, w)         # 計算, mag=增益關係，phase=相位關係    
plt.figure(figsize=(10,10),dpi=80)         #設定子圖配置
plt.subplot(212)			#子圖2
plt.subplots_adjust(wspace=0,hspace =0.35)#子圖一參數
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
plt.semilogx(f, phase)                          # 繪製頻率-增益曲線
        #標點(截止頻率)
	
plt.ylabel("Phase(deg)", fontweight = "bold",fontsize=12) #y座標
plt.hlines(135,0,10e4,linestyle= '--',colors = "r")    #畫水平線(y,xstart,xend)
plt.vlines(10e4,90,135,linestyle= '--',colors = "r")   #畫垂直線(x,ystart,yend)                 	
plt.scatter(10e4,135)
plt.annotate(r'         Cutoff frequency($f_b$)=6.283*10^4 (Hz)',#圖上註解
         xy=(10e4,135), xycoords='data',xytext=(+1, -1),c="b",
             textcoords='offset points', fontsize=13,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.annotate(r'         at phase=135(deg)',                        #圖上註解
         xy=(10e4,135), xycoords='data', xytext=(+13, -13),c="b",
             textcoords='offset points', fontsize=13,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.xlabel("Frequency(Hz)", fontweight = "bold",fontsize=12)#y軸

plt.subplot(211)			#子圖1
plt.semilogx(f,mag)                 # 繪製頻率-相位曲線
          #標點(截止頻率)
plt.title("Bode Diagram(Theorem)",fontweight = "bold",fontsize=16) 	#標題
plt.ylabel("Magnitude(dB)", fontweight = "bold",fontsize=12)        #y座標
plt.xlabel("Frequency(Hz)", fontweight = "bold",fontsize=12)     #X座標
plt.hlines(17,1,100000,linestyle= '--',colors = "r") #畫水平線(y,xstart,xend)
plt.vlines(100000,-60,17,linestyle= '--',colors = "r")       #畫垂直線(x,ystart,yend)             	
plt.scatter(100000,17)
plt.annotate(r'         Cutoff frequency($f_b$)=6.283*10^4 (Hz)',#圖上註解
         xy=(100000,17), xycoords='data',xytext=(+1, -1),c="b",
             textcoords='offset points', fontsize=13,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.annotate(r'         at Magnitude=17 dB',                        #圖上註解
         xy=(100000,17), xycoords='data', xytext=(+13, -13),c="b",
             textcoords='offset points', fontsize=13,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
plt.savefig("Bode Diagram ") #存檔名稱
plt.show()#顯示圖片
plt.close() 										




