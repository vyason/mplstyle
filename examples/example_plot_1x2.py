import numpy as np
from math import pi
import matplotlib.pyplot as plt

plt.style.use('vyason')
[def_width,def_height] = np.array(plt.rcParams["figure.figsize"])

fig = plt.figure(constrained_layout=True)
fig.set_size_inches(2*def_width,def_height)
ax = fig.add_gridspec(1,2,hspace=0.1,wspace=0.05).subplots()

xmin,xmax=0,2*pi
x = np.linspace(xmin,xmax,100,endpoint=True)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)*np.exp(-x)
y4 = np.cos(x)*np.exp(-x)

ax[0].plot(x,y1,c='black',ls='solid',label=r'$y_1$')
ax[0].plot(x,y2,c='red',ls='dashed',label=r'$y_2$')
ax[1].plot(x,y3,c='green',ls='dotted',label=r'$y_3$')
ax[1].plot(x,y4,c='blue',ls='dashdot',label=r'$y_4$')

for i in range(2):
    ax[i].set_xlim(xmin,xmax)
    ax[i].set_xlabel(r'$x$')
    ax[i].set_ylabel(r'$y$')
    ax[i].legend()
    ax[i].grid()

fig.savefig('example_plot_1x2.png')