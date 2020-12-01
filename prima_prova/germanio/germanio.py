import numpy
from math import exp,sqrt
from matplotlib import pyplot
from dati import V, e_V, I, e_I

#seaborn.set()

for i in range(0,15):
    e_V[i]=sqrt(e_V[i]**2+(0.03*V[i])**2)

pyplot.style.use('my_style')
#print(e_V)

pyplot.errorbar(V, I, e_I, e_V, fmt='ok')
pyplot.yscale('log')
pyplot.xlabel('Tensione [V]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Germanio')
#pyplot.legend()
pyplot.savefig('germanio.png')
