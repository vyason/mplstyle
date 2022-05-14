import numpy as np
from math import pi
import matplotlib.pyplot as plt

plt.style.use('vyason')
[def_width,def_height] = np.array(plt.rcParams["figure.figsize"])

fig,ax = plt.subplots(2,2,constrained_layout=True)
fig.set_size_inches(2*def_width,2*def_height)

xmin,xmax=0,2*pi
x = np.linspace(xmin,xmax,100,endpoint=True)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)*np.exp(-x)
y4 = np.cos(x)*np.exp(-x)

ax[0,0].plot(x,y1,c='black',ls='solid',label=r'$y_1$')
ax[0,1].plot(x,y2,c='red',ls='dashed',label=r'$y_2$')
ax[1,0].plot(x,y3,c='green',ls='dotted',label=r'$y_3$')
ax[1,1].plot(x,y4,c='blue',ls='dashdot',label=r'$y_4$')

for i in range(2):
    for j in range(2):
        ax[i,j].set_xlim(xmin,xmax)
        ax[i,j].set_xlabel(r'$x$')
        ax[i,j].set_ylabel(r'$y$')
        ax[i,j].legend()
        ax[i,j].grid()

fig.savefig('example_plot_2x2.png')
