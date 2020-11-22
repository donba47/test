# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:25:36 2020

@author: petertw89
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.stats as stats
import math

def f_1(x, A, B):


    return A*x + B  
plt.figure(figsize=(8,6),dpi=80)   
ib=[10,20,30,40,50]
vcc0=[0.5319,0.5629,0.5778,0.5887,0.5952]
vcc1=[0.572,0.5849,0.5927,0.5991,0.6038]
vcc3=[0.5975,0.6037,0.6077,0.6117,0.6144]
vcc6=[0.593,0.6185,0.5798,0.5791,0.6256]
vcc9=[0.615,0.6276,0.6298,0.5518,0.6332]
vcc12=[0.591,0.6345,0.6363,0.6374,0.6393]
plt.style.use("ggplot")     
plt.ylabel("Ib   (uA)", fontweight = "bold",fontsize=14)
plt.xlabel("Vbe   (Volt)", fontweight = "bold",fontsize=14)  

plt.title("transister Relationship between Vbe and Ib",
           fontweight = "bold",fontsize=16)        

#plt.scatter(vse0,ic0,c = "m",s = 50)
#plt.scatter(ib,vcc0,c = "m",s = 50) 
plt.plot(vcc0,ib)
plt.plot(vcc1,ib)
plt.plot(vcc3,ib)
plt.annotate(r'vcc=0V',
         xy=(0.5952,50), xycoords='data', xytext=(-30,+1),c="b",
             textcoords='offset points', fontsize=12)
plt.annotate(r'vcc=1V',
         xy=(0.6038,50), xycoords='data', xytext=(-20,+1),c="y",
             textcoords='offset points', fontsize=12)
plt.annotate(r'vcc=3V',
         xy=(0.6144,50), xycoords='data', xytext=(-20,+1),c="g",
             textcoords='offset points', fontsize=12)
#plt.scatter(vce6,ic6,c = "m",s = 50) 
#plt.plot(vce6,ic6)       
#plt.axhline(y=0,c='black')
#plt.axvline(x=0,c='black')                  
#A2,B2=optimize.curve_fit(f_1, x, y)[0]
#x2 = np.arange(-7,7,0.0001)
#y2 = A2*x2 + B2
#r=stats.pearsonr(x,y)
#plt.text(0.014,1.66, r'Correlation coefficient=%s'%(round(r[0],6)))
#print("Av=%s"%A2)
#Avdb=20*math.log(np.abs(A2),10)
#print("Av(dB)=%s"%Avdb)
   
#plt.text(2.5,5, r'Av=%s'%(round(A2,4)),fontsize=15)
#plt.text(2.5,4, r'Av|db=-0.07152',fontsize=15)     
plt.legend(loc="best")
plt.savefig("Relationship between ib and Vbe") 
plt.show()
plt.close() 

