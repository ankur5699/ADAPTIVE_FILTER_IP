#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:11:27 2024

@author: ankur
"""

# w(n+1) = w(n) +[(μ * e(n) * x(n)) / Eng]
# (1/M)*Σx(m)^2 
#Let adaptive filter have 64 taps
import numpy as np
import matplotlib.pyplot as plt


N = 64 #num_taps
num_samples = 64
quantization = 12 #bits


ENV_MODEL = np.random.randint(0,2**quantization,N)
w = np.random.randint(0,2**quantization,N)

ERROR_plot = []

data                = np.random.randint(0,2**quantization,num_samples)
desired_signal      = data * ENV_MODEL
output_signal       = data * w

for i in range(100):

    
    # ENERGY              = (1/num_samples) * np.sum(data*data) 
    ERROR               = (desired_signal - output_signal)
    w                   = w + ((0.001 * (ERROR) * data))
    # print(ERROR[0])
    # print(w[0])
    ERROR_plot.append(ERROR[0])
   
plt.plot(ERROR_plot)
plt.show()
    
    
