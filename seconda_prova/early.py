import numpy
import seaborn
from math import exp,sqrt
from matplotlib import pyplot
from ib100.linearfit import linearfit as lf1
from ib200.linearfit import linearfit as lf2
from ib100.dati import V as V1, e_V as e_V1, I as I1
from ib200.dati import V as V2, e_V as e_V2, I as I2


pyplot.style.use('my_style')

for i in range(0,33):
    e_V1[i] = sqrt(e_V1[i]**2+(0.03*V1[i])**2)
for i in range(0,24):
    e_V2[i] = sqrt(e_V2[i]**2+(0.03*V2[i])**2)

pyplot.errorbar(I1, V1, 0, e_V1, fmt='ok', label = 'dati $I_b = 100 \mu A$')
pyplot.errorbar(I2, V2, 0, e_V2, fmt='ok', label = 'dati $I_b = 200 \mu A$')
pyplot.yscale('linear') 
pyplot.ylabel('Tensione [V]')
pyplot.xlabel('Corrente [mA]')
pyplot.title('Effetto Early')

a1,b1,da1,db1=lf1(I1,V1,e_V1)
a2,b2,da2,db2=lf2(I2,V2,e_V2)

x=numpy.linspace(0,40,100)
pyplot.plot(x,a1+b1*x,label = 'fit $I_b = 100 \mu A$ ') 
pyplot.plot(x,a2+b2*x,label = 'fit $I_b = 200 \mu A$') 

pyplot.legend()
pyplot.savefig('effetto_early.png')


