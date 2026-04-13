import random
lst = []
for i in range(50):
  lst.append(random.randint(1,30))
print(lst)

for num in lst[:]:
  count = lst.count(num)
  if count > 1:
    for _ in range(count - 1):
        lst.remove(num)
print(f"list after removing duplicates: {lst}")
