# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:17:16 2019

@author: apereira2
"""
import time
def funcaoTeste(x):
    y = ((np.e)**x)-x-2
    return y

def deVfuncaoTeste(x):
    dy = (np.e**x)-1
    return dy

def Newt(x0):
    x1=1
    while True:
        x0 = x1
        x1 = x0 - (funcaoTeste(x0)/deVfuncaoTeste(x0))
        error = x1-x0
        print(x1)
        print(abs(error))
        
        if error < 0.0001:
            print('Raiz aproximada = {}'.format(x1))
            print('Error = {}'.format(abs(error)))
            print('código finalizado')
            break
        
inicio = time.time()
Newt(3)
fim = time.time()
print(fim-inicio)
        
    