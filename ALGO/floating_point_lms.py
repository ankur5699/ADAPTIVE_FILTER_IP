#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:47:56 2024

@author: ankur
"""

import numpy as np
import matplotlib.pyplot as plt

#num_taps
N = 10
u = 0.01
eps = 0.00001


ALGO = "LMS"


x = np.random.normal(0, 1, N)
ENV_MODEL = np.random.normal(0, 10, N)
w = np.random.normal(0, 1, N)

d = x * ENV_MODEL

ERROR_plot = []

for i in range(500):
    y = x * w
    e = d - y
    if ALGO == "LMS":
        w = w + u * x * e
    if ALGO == "NLMS":
        w = w + (u/(eps+(x*x))) * x * e
    e[e < 0.0001] = 0
    ERROR_plot.append(sum(np.square(e)))
plt.plot(ERROR_plot[-10:])
plt.show()

print(w)
print(ENV_MODEL)
