def recgcd(n,d):
  if n%d == 0:
    return d
  else:
    return recgcd(d, n%d)

n = int(input("Enter a number: "))
r = int(input("Enter another number: "))
print("GCD of",n,"and",r,"is",recgcd(n,r))
