#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def LeakyRelu(x):
    s = np.maximum(0.01*x,x)
    plt.plot(x,s)
    plt.xlabel('valus of x')
    plt.ylabel('LeakyRelu Values')
    plt.title('LeakyRelu Function')
    plt.legend(["Leaky Relu"])
    plt.show()
    return s


x = np.array(np.arange(-10,11,1))
s = print(LeakyRelu(x))

