import math
x=math.fmod(5,2)
print(x)
print(" ")
g=math.fmod(45,2)
print(g)
y=math.fmod(117,19)
print(y)
#trunc
r=math.trunc(-29.99)
print(r)
#square root
f=math.sqrt(121)
#integer square root
c=math.isqrt(121)
print(f)
print(c)
#frexp
#Return mantissa and exponent of numbers
#The mathematical formula for this method is: number = m * 2**e.
print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))
print(math.frexp(10))
#not a number(nan)
print(math.nan)
#is not a number(isnan)
h=math.isnan(math.nan)
print(h)
print(math.isnan(90))

