def recprime(n, d=2):
  if n<=1:
    return[]
  elif n%d == 0:
    return [d] + recprime(n//d, d)
  else:
    return recprime(n, d+1)

n = int(input("Enter a number: "))
print("Prime factors of",n, "are",recprime(n))
