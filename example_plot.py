import numpy as np
import matplotlib.pyplot as plt

plt.style.use('vyason')

x,y1,y2 = np.loadtxt('table.d',unpack=True)

plt.plot(x,y1,c='black',ls='-',label=r'$y_1$')
plt.plot(x,y2,c='red',ls='--',label=r'$y_2$')

plt.xlim(0,2);      plt.ylim(-20,30)
plt.xlabel(r'x');   plt.ylabel(r'y')
plt.grid();         plt.legend()

plt.savefig('example_plot.png')