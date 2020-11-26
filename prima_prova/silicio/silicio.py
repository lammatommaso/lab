import numpy
from math import exp
from matplotlib import pyplot
from dati import V, e_V, I, e_I

pyplot.errorbar(V, I, e_V, e_I)
pyplot.yscale('linear')
pyplot.xlabel('Tensione [V]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')
pyplot.legend()
pyplot.savefig('silicio.png')
