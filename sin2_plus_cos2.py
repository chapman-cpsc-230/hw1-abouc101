print "Part A"
from math import sin,cos
pi= 3.141592
x=pi/4
val= ((sin(x))**2 + (cos(x))**2)
print val

print "Part B"
v= 3 #m/s
t= 1 #s
a= 2 #m/s**2
s= v*t + .5*a*(t)**2
print s, "meters"

print "Part C"
a = 3.3
b = 5.3
A = (a)**2
B = (b)**2
E1SUM = A+2*a*b+B
print E1SUM
E2SUM = A-2*a*b+B
print E2SUM
E1POW = (a+b)**2
print E1POW
E2POW = (a-b)**2
print E2POW
