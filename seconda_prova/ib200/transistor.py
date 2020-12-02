import numpy
import seaborn
from math import exp,sqrt
from matplotlib import pyplot
from dati import V, e_V, I

pyplot.style.use('my_style')

for i in range(0,24):
    e_V[i] = sqrt(e_V[i]**2+(0.03*V[i])**2)

#print(e_V_osc)

pyplot.errorbar(V, I, 0, e_V, fmt='ok')
pyplot.yscale('linear') 
pyplot.xlabel('Tensione [V]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica in uscita')
#pyplot.legend()
pyplot.savefig('transistor.png')

