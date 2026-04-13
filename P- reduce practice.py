from functools import reduce
def sum(a,b):
  return a+b
def prod(a,b):
  return a*b
lst1 = [1,2,3,4,5]
s = reduce(sum,lst1)
p = reduce(prod,lst1)
print(lst1,s,p)


lst2 = [1,2,3,4,5]
s = reduce(lambda x,y: x+y,lst2)
print(s)


lst3 = [1,2,3,4]
p = reduce(lambda x,y: x*y,lst3)
print(p)
