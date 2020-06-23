#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def tanH(x):
    s = (1-np.exp(-x))/(1+np.exp(-x))
    plt.plot(x,s)
    plt.xlabel('valus of x')
    plt.ylabel('tanH values')
    plt.title('tanH Function')
    plt.legend(["Tanh"])
    plt.show()
    return s

def tanH_Derivative(x):
    s = (1-np.exp(-x))/(1+np.exp(-x))
    sd = 1 - s**2
    plt.plot(x,sd)
    plt.xlabel('valus of x')
    plt.legend(["Tanh Derivative"])
    plt.ylabel('TanH_Derivative values')
    plt.title('TanH_Derivative Function')
    plt.show()
    return sd

x = np.array(np.arange(-10,11,1))
s = print(tanH(x))
sd = print(tanH_Derivative(x))


# In[ ]:




