#!/usr/bin/python

#print vars()

print(vars())

print("%s"%(vars()))
a=10
print("%s"%(vars()))
b=20

import math
print(math.cos(a))
from math import cos
print(cos(a)) 
from math import cos as cos_V1
print(cos_V1(a)) 

from math import *
print(cos(a))

from math import math_V1
print(math_V1(a)) 

