#filename:function.py

print(abs(100))
print(abs(-100))
print(abs(12.34))

print(max(1,2))
print(max(1,2,3,-4))

print(int('123'))
print(int(12.34))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

def myabs(x):
    if x>=0:
       return x
    else:
       return -x

print(myabs(-4))

def nop():
    pass

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
       return x
    else:
       return -x

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,60)
print(x,y)