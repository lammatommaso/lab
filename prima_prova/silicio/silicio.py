import numpy
import seaborn
from math import exp
from matplotlib import pyplot
from dati import V, e_V, I, e_I

seaborn.set()

pyplot.errorbar(V, I, e_I, e_V, fmt='.k')
pyplot.yscale('log')
pyplot.xlabel('Tensione [V]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')
pyplot.legend()
pyplot.savefig('silicio.png')
