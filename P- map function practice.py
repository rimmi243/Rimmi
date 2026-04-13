lst = [1,2,3,4,5]
result = list(map(lambda x: x*x,lst))
print(result)


c = [0,10,20,30]
f = list(map(lambda x: (9/5)*x+32,c))
print(f)


import math
def func1(n):
  return n*n
lst = [5,10,15,20,25]
m1 = map(math.radians,lst)
m2 = map(math.factorial,lst)
m3 = map(func1,lst)
print(list(m1))
print(list(m2))
print(list(m3))
