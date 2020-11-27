import numpy
import seaborn
from math import exp
from matplotlib import pyplot
from dati import V_mul, e_V_mul, V_osc, e_V_osc

seaborn.set()

pyplot.errorbar(V_mul, V_osc, e_V_osc, e_V_mul, fmt='.k')
pyplot.yscale('linear') 
pyplot.xlabel('Tensione Multimetro [V]')
pyplot.ylabel('Corrente Oscilloscopio [V]')
pyplot.title('Calibrazione Oscilloscopio-Multimetro')
pyplot.legend()
pyplot.savefig('calibrazione.png')

