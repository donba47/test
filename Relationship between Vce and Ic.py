# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:25:36 2020

@author: petertw89
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
plt.figure(figsize=(8,6),dpi=80)  
vce1=[-71.91e-3,0.9964,2.974,5.993,8.97,11.973]
vce2=[3.95e-3,50.57e-3,0.1109,2.264,5.229,8.157]
vce3=[0.13e-6,24.93e-3,49.36e-3,75.86e-3,103.63e-3,0.1913]
vce4=[1.96e-3,17.12e-3,35.24e-3,53.97e-3,69.40e-3,84.29e-3]
vce5=[1.24e-3,12.61e-3,35.62e-3,49.35e-3,56.08e-3,67.06e-3]
vce6=[1.41e-3,10.77e-3,23.25e-3,37.32e-3,47.87e-3,57.17e-3]

ic1=[-0.14e-3,34.51e-3,182.53e-3,0.4712,0.8349,1.3239]
ic2=[9.68e-3,107.35e-3,0.2791,0.5518,0.8955,1.3551]
ic3=[10.11e-3,164.08e-3,0.3586,0.6353,0.9668,1.4157]
ic4=[0.58e-3,169.22e-3,0.4296,0.7139,1.0366,1.4595]
ic5=[-10.24e-3,0.1876,0.4938,1.1033,1.3551,1.4995]
ic6=[-9.77e-3,0.1956,0.5658,0.8744,1.17781,1.5560]
plt.style.use("ggplot")     
plt.xlabel("Vce   (Volt)", fontweight = "bold",fontsize=14)
plt.ylabel("Ic   (mA)", fontweight = "bold",fontsize=14)  

plt.title("Relationship between Vce and Ic in Saturation",
           fontweight = "bold",fontsize=16)        
vcee=[11.973,8.157,0.1913,84.29e-3,67.06e-3,57.17e-3]
vcc=9
icc=[34.51e-6,107.35e-6,164.08e-6,169.22e-6,0.1876e-3,0.1956e-3]
ic=np.linspace(0,9/5000,50)
vo=vcc-ic*5000
ic=ic*1000
#plt.annotate(r'Ib=20ua',xy=(0.1913,1.4157), xycoords='data', xytext=(-20,10),c="b",textcoords='offset points', fontsize=12)
#plt.annotate(r'Ib=30ua',xy=(84.29e-3,1.4595), xycoords='data', xytext=(+10,+1),c="b",textcoords='offset points', fontsize=12)
#plt.annotate(r'Ib=40ua',xy=(67.06e-3,1.4995), xycoords='data', xytext=(-2,+8),c="b",textcoords='offset points', fontsize=12)
#plt.annotate(r'Ib=50ua',xy=(57.17e-3,1.5560), xycoords='data', xytext=(-20,+10),c="b",textcoords='offset points', fontsize=12)
plt.scatter(vce2,ic2,c = "m",s = 50) 
plt.plot(vce2,ic2)  
plt.scatter(vce1,ic1,c = "m",s = 50) 
plt.plot(vce1,ic1)
plt.plot(vce3,ic3)
plt.plot(vce4,ic4)
plt.plot(vce5,ic5)
plt.plot(vce6,ic6)
plt.plot(vo,ic,"--")
plt.annotate(r'ib=10ua',xy=(8.157,1.3551), xycoords='data', xytext=(+15,0),c="b",textcoords='offset points', fontsize=12)
plt.annotate(r'ib<10ua',xy=(11.973,1.3239), xycoords='data', xytext=(-20,+10),c="b",textcoords='offset points', fontsize=12)
plt.annotate(r'Load line(vcc=9v)',xy=(2,1.5), xycoords='data', xytext=(-20,+10),c="b",textcoords='offset points', fontsize=12)    
plt.axhline(y=0,c='black')
plt.axvline(x=0,c='black')                  
plt.legend(loc="best")
plt.savefig("Relationship between Vce and Ic in Saturation") 
plt.show()
plt.close() 

