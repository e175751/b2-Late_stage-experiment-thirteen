import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("c_returnmap.txt",header=None)
plt.xlim(0,1)
plt.ylim(0,1)
x_fun = np.arange(0,1.1,0.001)
y_fun = 1.50 * (1-x_fun)*x_fun
x_line = np.arange(0, 1.1, 0.1)
y_line = x_line
plt.plot(x,y,x_line,y_line,x_fun,y_fun)
plt.savefig("r_1.50.png")


plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,y,".",markersize=1)
plt.savefig("s_1.50.png")
