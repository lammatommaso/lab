import numpy
import seaborn
from math import exp,sqrt
from matplotlib import pyplot
from dati import V_mul, e_V_mul, V_osc, e_V_osc

pyplot.style.use('my_style')

for i in range(0,9):
    e_V_osc[i] = sqrt(e_V_osc[i]**2+(0.03*V_osc[i])**2)

#print(e_V_osc)

pyplot.errorbar(V_mul, V_osc, e_V_osc, e_V_mul, fmt='ok')
pyplot.yscale('linear') 
pyplot.xlabel('Tensione Multimetro [V]')
pyplot.ylabel('Tensione Oscilloscopio [V]')
pyplot.title('Calibrazione Oscilloscopio-Multimetro')
#pyplot.legend()
pyplot.savefig('calibrazione.png')

