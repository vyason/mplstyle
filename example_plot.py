import numpy as np
import matplotlib.pyplot as plt

plt.style.use('vyason')

fig = plt.figure(constrained_layout=True)
ax = fig.subplots()

x,y1,y2 = np.loadtxt('table.d',unpack=True)

ax.plot(x,y1,c='black',ls='-',label=r'$y_1$')
ax.plot(x,y2,c='red',ls='--',label=r'$y_2$')

ax.set_xlim(0,2);           ax.set_ylim(-20,30)
ax.set_xlabel(r'$x$');      ax.set_ylabel(r'$y$')
ax.grid();                  ax.legend()

fig.savefig('example_plot.png')