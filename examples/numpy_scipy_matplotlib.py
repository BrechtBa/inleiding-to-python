import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,50)

# build an array elementwise
c = np.zeros_like(x)
for i,xi in enumerate(x):
	c[i] = np.cos(xi)

# vectorized functions
s = np.sin(x)

ss = scipy.integrate.cumtrapz(c,x)

# plotting parameters
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=8)
plt.rc('figure', autolayout=True)

# plotting
plt.figure(figsize=(10/2.54,7/2.54))
plt.plot(x,c,label=r'cosinus')
plt.plot(x,s,'-s',label=r'sinus')
plt.plot(x[1:],ss,label=r'$\int$ cosinus$(x)$ d$x$',linewidth=2)
plt.gca().set_xlabel(r'$x$ (rad)')
plt.gca().set_ylabel(r'$y$')
plt.legend(numpoints=1)

plt.savefig('sinus_cosinus.pdf')
plt.show()
