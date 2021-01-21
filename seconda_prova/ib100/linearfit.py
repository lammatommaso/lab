# MODULE LINEARFIT
from math import sqrt

def linearfit(x,y,e_y):
    S1=0
    Sx=0
    Sy=0
    Sxx=0
    Sxy=0
   
    for i in range(3,14):
                S1+=1/(e_y[i]**2)
                Sx+=x[i]/(e_y[i]**2)
                Sy+=y[i]/(e_y[i]**2)
                Sxx+=(x[i]**2)/(e_y[i]**2)
                Sxy+=(x[i]*y[i])/(e_y[i]**2)

    D=S1*Sxx-Sx**2

    a=(Sy*Sxx-Sx*Sxy)/D
    b=(S1*Sxy-Sx*Sy)/D
    da=sqrt(Sxx/D)
    db=sqrt(S1/D)

    return a,b,da,db
    

