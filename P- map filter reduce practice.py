lst1 = [1,2,3,4,5]
m = list(map(lambda x: x*x,lst1))
print(m)

f = list(filter(lambda x: x%5==0,lst1))
print(f)

from functools import reduce
lst = [1,2,3,4,5]
s2 = reduce(lambda x,y: x+y,lst)
p2 = reduce(lambda x,y: x*y,lst)
print(lst,s2,p2)



def sqr_g1000(n):
  return n>1000
lst = [10,20,30,40,50]
y = list(filter(sqr_g1000,map(lambda z: z*z,lst)))
print(y)
