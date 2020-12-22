import numpy
from linearfit import linearfit as lf
from math import exp,sqrt,log
from matplotlib import pyplot
from dati import V, e_V, I, e_I

for i in range(0,14):
    e_V[i]=sqrt(e_V[i]**2+(0.03*V[i])**2)*1000
    V[i]*=1000
  
pyplot.style.use('my_style')

pyplot.errorbar(V, I, e_I, e_V, fmt='ok',label = 'dati')
pyplot.yscale('log')
pyplot.xlabel('Tensione [mV]')
pyplot.ylabel('Corrente [mA]')
pyplot.title('Caratteristica I-V del diodo al Silicio')

#b , a = numpy.polyfit(numpy.log(I),V,1)
a,b,da,db,dab=lf(numpy.log(I),V,e_V)

print("a = ",a)
print("da = ",da)
print("b = ",b)
print("db = ",db)

I0=exp(-a/b)
dI0 = sqrt((I0*da/b)**2 + (a*I0*db/b**2)**2 + 2*(I0/b)*(I0*a/b**2)*dab)
print('I0 = ',I0)
print('dI0 = ',dI0)

x=numpy.linspace(50,350,100)
pyplot.plot(x,I0*(numpy.exp(x/b)-1),label = 'fit') 

# Dato che V = -clnI0+clnI abbiamo che V=cln(I/I0), I/I0 = e^(V/c-1)

pyplot.legend()
pyplot.savefig('grafico_silicio.png')
