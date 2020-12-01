import numpy
import seaborn
from math import exp,sqrt
from matplotlib import pyplot
from dati import V, e_V, I, e_I

for i in range(0,14):
    e_V[i]=sqrt(e_V[i]**2+(0.03*V[i])**2)

#print(e_V)

#seaborn.set()
pyplot.style.use('my_style')

pyplot.errorbar(V, I, e_I, e_V, fmt='ok')
pyplot.yscale('log')
pyplot.xlabel('Tensione [V]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')
#pyplot.legend()
pyplot.savefig('silicio.png')
