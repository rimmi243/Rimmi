def recsod(n):
  if n==0:
    return 0
  else:
    return n%10 + recsod(n//10)

n = int(input("Enter a number:"))
print("Sum of digits of",n,"is",recsod(n))
s=0
for digit in str(n):
  s=s+int(digit)
print(s)
