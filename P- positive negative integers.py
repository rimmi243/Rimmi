import random
lst=[]
for i in range(30):
  lst.append(random.randrange(-100,100))
print("Main List", lst)

p_list=[]
n_list=[]
for i in lst:
  if i>0:
    p_list.append(i)
  elif i<0:
    n_list.append(i)
print("list of positive integers: ", p_list)
print("list of negative integers: ", n_list)
