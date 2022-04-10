import numpy as np
import matplotlib.pyplot as plt
plt.style.use('vyason')

fig = plt.figure(constrained_layout=True)

table1 = np.genfromtxt('table1.d')
plt.plot(table1[:,0],table1[:,1],c='black',ls='-',label='Table 1')

table2 = np.genfromtxt('table2.d')
plt.plot(table2[:,0],table2[:,1],c='red',ls='--',label='Table 2')

plt.xlim(0,2)
plt.ylim(-20,30)
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.grid()
plt.legend()

plt.savefig('example_plot.png')