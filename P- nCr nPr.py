n = int(input("enter n: "))
r = int(input("enter r: "))
def factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact *= 1
  return fact


def nCr(n,r):
  if r<0 or r>n:
    return 0
  else:
    return factorial(n)// (factorial(r) * factorial(n-r))

def nPr(n,r):
  if r<0 or r>n:
    return 0
  else:
    return factorial(n)// factorial(n-r)

print({n}C{r} = {nCr(n,r)})
print({n}P{r} = {nPr(n,r)})
  
