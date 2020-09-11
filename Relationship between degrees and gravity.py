# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:12:43 2020

@author: petertw89
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
def f_1(x, A, B):


    return A*x + B  
plt.figure(figsize=(8,6),dpi=250)   
x=[0.000196,0.000392,0.000490,0.000686,0.000882]
y=[124,243,335,430,570]
plt.style.use("ggplot")     
plt.ylabel("degrees_theta", fontweight = "bold",fontsize=14)
plt.xlabel("gravity_N", fontweight = "bold",fontsize=14)  

plt.title("Relationship between gravity and degrees",
           fontweight = "bold",fontsize=16)        

plt.scatter(x,y,c = "m",s = 50)                          
A2,B2=optimize.curve_fit(f_1, x, y)[0]
x2 = np.arange(0.000196,0.000882,0.00000001)
y2 = A2*x2 + B2
print(A2,B2)
plt.xlim(0.000168,0.000920)
plt.ylim(106,620)
plt.plot(x2, y2,"--",label="y=%s*x+%s"%(round(A2,9),round(B2,9)))     
plt.legend(loc="best")
plt.savefig("Relationship between degrees and gravity.jpg") 
plt.show()
plt.close() 