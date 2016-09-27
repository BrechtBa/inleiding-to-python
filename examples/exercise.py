#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# parameters
T0 = 80.
Ta = 20.

C = 100e3
h = 8.
k = 0.04
A = 6.

# create a time array
dt = 600.
t = np.arange(0.,24*3600.+dt,dt)



# define a function which integrates the heat loss equation
def heat_loss_ode_solution(t,T0,par):
    """
    Solves the heat loss equation
    
    Parameters
    ----------
    t : np.array
        time array
        
    Ti : float
        initial value for the temperature
    
    par : dict
        dictionary with parameters
        
    """
 
    T = np.zeros_like(t)
    T[0] = T0
    
    UA = 1/(1./par['h'] + par['d']/par['k'])*par['A']
    
    for i in range(len(t)-1):
        T[i+1] = T[i] + UA/par['C']*(par['Ta']-T[i])*(t[i+1]-t[i])
        
    return T



      
# calculate the values for all insulation thickness values
T = []
d = np.linspace(0.0,0.2,5)

for di in d:
    temp = heat_loss_ode_solution(t,T0,{'h': h, 'k': k, 'd':di, 'A':A, 'C': C, 'Ta': Ta})
    T.append(temp)
    
    
# plot 
for di,Ti in zip(d,T):     
    plt.plot( t/3600.,Ti,label='d = {:.2f}m'.format(di) )

plt.legend()
plt.xlabel('$t$ (h)')
plt.ylabel('$T$ ($^\circ$C)')
plt.show()