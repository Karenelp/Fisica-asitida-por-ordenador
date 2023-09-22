# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:24:21 2023

@author: kaths
"""

n = int(input("Dime un número entero:"))
if n%2==0:
    print(n,"es un número par")
    if n==6:
        print("Qué poco creativo")
    else:
        print("pero podías pensar en algo más original")
else :
    print (n,"es un número impar")
    print ("y por tanto, has perdido mis  respetos")