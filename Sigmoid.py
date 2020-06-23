#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# 1(a) Sigmoid
def sigmoid(x):
    s = 1/(1+np.exp(-x))
    plt.plot(x,s)
    plt.xlabel('valus of x')
    plt.ylabel('sigmoid Values')
    plt.title('Sigmoid Function')
    plt.legend(["Sigmoid"])
    plt.show()
    return s

def Sigmoid_Derivative(x):
    s = 1/(1+np.exp(-x))
    sd = s*(1-s)
    plt.plot(x,sd)
    plt.xlabel('valus of x')
    plt.ylabel('sigmoid_Derivative Values')
    plt.title('Sigmoid_Derivative Function')
    plt.legend(["SigmoidDerivativs"])
    plt.show()
    return sd

x = np.array(np.arange(-10,11,1))
s = print(sigmoid(x))
sd = print(Sigmoid_Derivative(x))


# In[ ]:




