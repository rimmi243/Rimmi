import random
even_list=[]
odd_list=[]
for i in range(5):
   odd_list.append(random.randrange(1,100,2))
print(odd_list)
for i in range(4):
   even_list.append(random.randrange(2,100,2))
print(even_list)

odd_list[2:3] = even_list
print(odd_list)
odd_list.sort()
print(odd_list)

   
