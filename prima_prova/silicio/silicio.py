import numpy
from math import exp
from matplotlib import pyplot

#pyplot.scatter(V_2, i_2, label = 'linear')
pyplot.yscale('log')
pyplot.xlabel('Tensione [mV]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')
pyplot.legend()
pyplot.savefig('silicio.png')
