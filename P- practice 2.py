s=input("enter your name:")
print(s)
vowels= "'a','e','i','o','u','A','E','I','O','U'"
count=0
for char in s:
  if char in vowels:
      count+=1
return count
print(count)
