#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

z=np.arange(-20,21,1)
def PRelu(z):
    def prelu(z,alpha):
        if(z<0):
            return(alpha*z)
        else:
            return z
    def derivative_prelu(z,alpha):
        if(z<0):
            return alpha
        else:
            return 1 
        
    f=[prelu(i,alpha=0.1) for i in z]
    df=[derivative_prelu(i,alpha=0.1) for i in z]
    #return f

    plt.plot(z,f)
    plt.plot(z,df)
    plt.legend(["PRelu", "PRelu Derivative"])
    plt.show()
    
PRelu(z)

