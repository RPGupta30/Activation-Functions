#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def softmax(z):
    dem=0
    for i in z:
        dem=dem+np.exp(i)
        
    g=np.sum(np.exp(z),axis=0)    
    f=[(np.exp(i)/dem) for i in z]
    df=[(g*(np.exp(i)/dem)) for i in z]
    #return f
    plt.plot(z,f)
    plt.plot(z,df)
    plt.legend(["softmax", "softmax_deri"])
    plt.show()

    
softmax(z)

