def recfibo(n):
  if n==1 or n==2:
    return 1
  else:
    return recfibo(n-1) + recfibo(n-2)
for x in range(1,11):
  print(recfibo(x))
