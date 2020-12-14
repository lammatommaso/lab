import numpy
from math import exp,sqrt
from matplotlib import pyplot
from dati import V_mul, e_V_mul, V_osc, e_V_osc
from linearfit import linearfit as lf

pyplot.style.use('my_style')

for i in range(0,9):
    e_V_osc[i] = sqrt(e_V_osc[i]**2+(0.03*V_osc[i])**2)
    
a,b,da,db=lf(V_mul,V_osc,e_V_osc)

print("a = ",a)
print("da = ",da)
print("b = ",b)
print("db = ",db)


x = numpy.linspace(0.1,0.8,100)
pyplot.errorbar(V_mul, V_osc, e_V_osc, e_V_mul, fmt='ok', label='dati')
pyplot.plot(x,a+b*x, label='fit')
pyplot.yscale('linear') 
pyplot.xlabel('Tensione Multimetro [V]')
pyplot.ylabel('Tensione Oscilloscopio [V]')
pyplot.title('Calibrazione Oscilloscopio-Multimetro')
pyplot.legend()
pyplot.savefig('grafico_calibrazione.png')

