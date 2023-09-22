# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:24:21 2023

@author: kaths
"""

#Dar las soluciones reales a un polinomio de segundo grado (from math import sqrt)
#e indicar si no existen.
#Extender el programa para dar soluciones complejas

from cmath import sqrt as cs
from math import sqrt as s

print("ax^2+bx+c")

#Primero definiremos las variables

a=float(input('Valor de a:'))
b=float(input('Valor de b:'))
c=float(input('Valor de c:'))

#Calcular el discriminante
discriminante=float((b**2)-4*a*c)
#Condicionar las soluciones reales


if discriminante>0:
    R1=(-b + s(discriminante))/(2*a)
    R2=(-b - s(discriminante))/(2*a)
    print('Las soluciones son:',R1, 'y', R2)
elif discriminante==0:
    R3=-b/(2*a)
    print('Hay una solución doble:',R3)
else :
    R4=(-b + cs(discriminante))/(2*a)
    R5=(-b - cs(discriminante))/(2*a)
    print ('Las soluciones son complejas:',R4, 'y',R5)
    
    


    
    