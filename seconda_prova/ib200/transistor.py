import numpy
import seaborn
from math import exp,sqrt
from matplotlib import pyplot
from linearfit import linearfit as lf
from dati import V, e_V, I

pyplot.style.use('my_style')

for i in range(0,24):
    e_V[i] = sqrt(e_V[i]**2+(0.03*V[i])**2)

pyplot.errorbar(I, V, 0, e_V, fmt='ok', label = 'dati')
pyplot.yscale('linear') 
pyplot.ylabel('Tensione [V]')
pyplot.xlabel('Corrente [mA]')
pyplot.title('Caratteristica in uscita($ I_B = 200 \mu A$)')

a,b,da,db=lf(I, V ,e_V)

print("a = ",a)
print("da = ",da)
print("b = ",b)
print("db = ",db)

x=numpy.linspace(33,40,100)
pyplot.plot(x,a+b*x,label = 'fit') 

pyplot.legend()
pyplot.savefig('grafico_transistor.png')


