import numpy as np
import matplotlib.pyplot as plt

plt.style.use('vyason')
[def_width,def_height] = np.array(plt.rcParams["figure.figsize"])

fig = plt.figure(constrained_layout=True)
fig.set_size_inches(2*def_width,def_height)
ax = fig.add_gridspec(1,2,hspace=0).subplots()

x,y1,y2 = np.loadtxt('table.d',unpack=True)

ax[0].plot(x,y1,c='black',ls='-',label=r'$y_1$')
ax[1].plot(x,y2,c='red',ls='--',label=r'$y_2$')

for i in range(2):
    ax[i].set_xlim(0,2);       ax[i].set_ylim(-20,30)
    ax[i].set_xlabel(r'$x$');
    ax[i].grid();

ax[0].set_ylabel(r'$y_1$')
ax[1].set_ylabel(r'$y_2$')

fig.savefig('example_plot_2cols.png')