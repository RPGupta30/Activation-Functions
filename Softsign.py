#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def SoftSign(x):
    s = x/(1+abs(x))
    plt.plot(x,s)
    plt.xlabel('valus of x')
    plt.ylabel('SoftSign Values')
    plt.title('SoftSign Function')
    plt.legend(["Softsign"])
    plt.show()
    return s

def SoftSign_Derivative(x):
    sd = 1/(1+(abs(x))**2)
    plt.plot(x,sd)
    plt.xlabel('valus of x')
    plt.ylabel('SoftSign_Derivative Values')
    plt.title('SoftSign_Derivative Function')
    plt.legend(["Softsign Derivative"])
    plt.show()
    return sd

x = np.array(np.arange(-10,11,1))
s = print(SoftSign(x))
sd = print(SoftSign_Derivative(x))


# In[ ]:





# In[ ]:




