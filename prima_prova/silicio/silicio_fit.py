import numpy
from scipy.optimize import curve_fit
from linearfit import linearfit as lf
from math import exp,sqrt,log
from matplotlib import pyplot
from dati import V, e_V, I, e_I

def my_function(x,a,b):
    return a*numpy.exp(x/b-1)

for i in range(0,14):
    e_V[i]=sqrt(e_V[i]**2+(0.03*V[i])**2)*1000
    V[i]*=1000
  
pyplot.style.use('my_style')

pyplot.errorbar(V, I, e_I, e_V, fmt='ok')
pyplot.yscale('log')
pyplot.xlabel('Tensione [mV]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')
#pyplot.legend()

popt, _ = curve_fit(my_function, V, I, p0=(0,40))
a, b = popt

print(a,b)

vexp=numpy.vectorize(exp)
x=numpy.linspace(50,350,100)
pyplot.plot(x,my_function(x,a,b)) 

# Dato che V = -clnI0+clnI abbiamo che V=cln(I/I0), I/I0 = e^(V/c-1)

pyplot.savefig('silicio.png')