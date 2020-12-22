# MODULE LINEARFIT
from math import sqrt

def linearfit(x,y,e_x):
    S1=0
    Sx=0
    Sy=0
    Sxx=0
    Sxy=0
   
    for i in range(0,15):
        S1+=1/(e_x[i]**2)
        Sx+=x[i]/(e_x[i]**2)
        Sy+=y[i]/(e_x[i]**2)
        Sxx+=(x[i]**2)/(e_x[i]**2)
        Sxy+=(x[i]*y[i])/(e_x[i]**2)

    D=S1*Sxx-Sx**2

    a=(Sy*Sxx-Sx*Sxy)/D
    b=(S1*Sxy-Sx*Sy)/D
    da=sqrt(Sxx/D)
    db=sqrt(S1/D)
    dab=-Sx/D

    return a,b,da,db,dab
    

