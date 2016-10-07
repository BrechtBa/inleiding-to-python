#!/usr/bin/env python
# 
# Dit script berekent het temperatuursverloop van een massa die afkoelt in een
# omgeving met constante temperatuur voor verschillende isolatiediktes
#

# packages importeren
import numpy as np
import matplotlib.pyplot as plt

################################################################################
# Parameters
################################################################################
T0 = 80.            # Begin temperatuur [degC]
Ta = 20.            # Omgevingstemperatuur [degC]

C = 100e3           # Warmtecapaciteit van de massa [J/K]
h = 8.              # Convectie coefficient [W/m2 K]
k = 0.04            # Thermische geleidbaarheid van het isolatiemateriaal [W/m K]
A = 6.              # Oppervlakte [m2]
dmin = 0.00         # Minimale isolatiedikte [m]
dmax = 0.20         # Maximale isolatiedikte [m]
nd = 5              # Aantal diktes [-]

tf = 24*3600        # Eindtijd [s]
dt = 600            # Tijdstap [s]



################################################################################
# Functies
################################################################################
# aangezien er voor dit probleem slechts 1 functie nodig is, is het niet
# interessant om deze in een appart bestand op te slaan en te importeren.
# Wanneer meerdere functies nodig zijn is dit wel interessant.
def heat_loss_ode_solution(t,T0,Ta,UA,C):
    """
    Geeft het temperatuursverloop van een massa die afkoelt in een omgeving op
    constante temperatuur in functie van de tijd.
    
    Parameters
    ----------
    t : np.array
        tijd array
        
    T0 : number
        beginwaarde voor de temperatuur [degC] of [K], de eenheid moet
        overeenkomen met die van Ta
    
    Ta : number
        omgevingstemperatuur [degC] of [K], de eenheid moet overeenkomen met die
        van T0
    
    UA : number
        thermishe geleidbaarheid tusse massa en omgeving [W/K]
        
    C : number
        warmtecapaciteit van de massa [J/K]
        
    """
 
    T = np.zeros_like(t)
    T[0] = T0
    
    for i in range(len(t)-1):
        T[i+1] = T[i] + UA/C*(Ta-T[i])*(t[i+1]-t[i])
        
    return T

    
    
################################################################################
# Berekeningen
################################################################################
# maak een tijd array
t = np.arange(0.,tf+dt,dt)

# initialiseer een list voor de temperatuursverlopen en een array met diktes
T = []
d = np.linspace(dmin,dmax,nd)

# voor elke dikte berekenen we de UA waarde en het temperatuursverloop en voegen dit toe aan de T list
for di in d:
    UA = (1./h + di/k)**-1*A 
    temp = heat_loss_ode_solution(t,T0,Ta,UA,C)
    T.append(temp)
    
    
    
################################################################################
# Plots
################################################################################
# plot het temperatuursverloop voor elke dikte
for di,Ti in zip(d,T):     
    plt.plot( t/3600.,Ti,label='d = {:.2f}m'.format(di) )

plt.legend()
plt.xlabel('$t$ (h)')
plt.ylabel('$T$ ($^\circ$C)')
plt.show()
