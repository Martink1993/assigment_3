mport numpy as np
import matplotlib.pyplot as plt
path = "C:\\Users\monster\Accelerators\2016-07-11_ipm_data.txt"
Dt = np.genfromtxt(path, delimiter = ' ')
fig, a = plt.subplots() 
a.plot(dt)
xmax = max(dt)
ymax = np.where(dt== xmax)
a.plot(ymax, xmax, 'ro')
plt.title('ionisation beam profile monitor (IPM)')
plt.grid(color='black', linestyle='-', linewidth=1)
fig = plt.show
plt.savefig('IPM.png')
