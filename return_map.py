import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
init=0.7
r=3.80
for i in range(0,101):
    if i%2==0:
        x.append(init)
        init=r*(1-init)*init
        y.append(init)
    else:
        x.append(init)
        y.append(init)

