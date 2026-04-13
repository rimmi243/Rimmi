def recfact(n):
  if n==0:
    return 1
  else:
    return n * recfact(n-1)
for x in range (11):
  print (f'{x:>2}! = {recfact(x):>10}')
