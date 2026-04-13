import random
odd=[]
even=[]
for i in range(1,5):
  odd.append(random.randrange(1,19,2))
  even.append(random.randrange(2,20,2))
print(odd)
#print(odd[1])
odd[2]=even
print(even)
print(odd)
flat_list=[]
for i in odd:
  
  if isinstance(i, list):
    for j in i:
      flat_list.append(j)
    else:
      flat_list.append(i)
print(flat_list)
print("Sorted List: ")
flat_list.sort()
print(flat_list)
      
