import numpy
from math import exp
from matplotlib import pyplot
from dati import V, e_V, I, e_I 

x = numpy.linspace(0, 2, 100)
R_1 = 1
#pyplot.errorbar(V_1, i_1, e_V_1, e_i_1, barsabove=True, uplims=True, lolims=True, ls = 'none', fmt = '.', capthick = 1)
pyplot.plot(x, R_1*x, label = 'fit')
pyplot.yscale('linear') #log otherwise
pyplot.xlabel('Tensione [mV]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Calibrazione Oscilloscopio-Multimetro')
pyplot.legend()
pyplot.savefig('calibrazione.png')

