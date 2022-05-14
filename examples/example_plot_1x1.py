import numpy as np
from math import pi
import matplotlib.pyplot as plt

plt.style.use('vyason')

fig,ax = plt.subplots(1,1,constrained_layout=True)

xmin,xmax=0,2*pi
x = np.linspace(xmin,xmax,100,endpoint=True)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)*np.exp(-x)
y4 = np.cos(x)*np.exp(-x)

ax.plot(x,y1,c='black',ls='solid',label=r'$y_1$')
ax.plot(x,y2,c='red',ls='dashed',label=r'$y_2$')
ax.plot(x,y3,c='green',ls='dotted',label=r'$y_3$')
ax.plot(x,y4,c='blue',ls='dashdot',label=r'$y_4$')

ax.set_xlim(xmin,xmax)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.legend()
ax.grid()


fig.savefig('example_plot_1x1.png')
