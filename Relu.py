#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def Relu_Function(x):
    s = np.maximum(x,0)
    plt.plot(x,s)
    plt.xlabel('valus of x')
    plt.ylabel('Relu_Function Values')
    plt.title('Relu_Function Function')
    plt.legend(["Relu"])
    plt.show()
    return s


x = np.array(np.arange(-10,11,1))
s = print(Relu_Function(x))

