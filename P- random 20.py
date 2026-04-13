import random
lst=[]
for i in range(20):
   lst.append(random.randrange(1,100))
print(lst)
num = int(input("Enter a number to search for: "))

for index, number in enumerate(lst):
  if number == num:
    print(f"{index}, {number}")
