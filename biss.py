# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
from time import sleep
import time

def funcaoTeste(x):
    y = ((np.e)**x)-x-2
    return y

def funcaoTeste2(x):
    y = ((x/2)**2)-np.sin(x)
    return y


def biss(a, b, f):
    print('######################')
    print('#  Bisection Method  #')
    print('######################')
          
    if f(a)*f(b) < 0:    
        print('According to Bolzano theorem, there is at least one real root inside this interval')
        if f(a) == 0:
            print('The number {} is a root.'.format(a))
        elif f(b) == 0:
            print('The number {} is a root.'.format(b))
        else:
            ite=0
            while True:
                ite+=1
                #sleep(1)
                e=abs(b-a)
                print('.')
                print('Error = {}'.format(e))
                x = (a+b)/2
                print('Aproximated root {}'.format(x))
                print('Number of iterations = {}'.format(ite))
                if f(a)<0 and f(x)<0:
                    a=x
                elif f(a)>0 and f(x)>0:
                    a=x
                if f(b)<0 and f(x)<0:
                    b=x
                elif f(b)>0 and f(x)>0:
                    b=x
                if e < 0.000001:
                    print(x)
                    print('End of iterations.')
                    break
begining1=time.time()
biss(1,2,funcaoTeste2)
end1=time.time()
print('Time of processing = {}seconds.'.format(end-begining))
begining2=time.time()
biss(1,2,funcaoTeste)
end2=time.time()
print('Time of processing = {}seconds.'.format(end-begining))

                    
                    
                
                
                
    