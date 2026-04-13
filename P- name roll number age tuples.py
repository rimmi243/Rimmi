lst=[
    (1,"Aarti",19),
    (2,"Sam",19),
    (3,"Neha",20),
    (4,"Amit",20)
    ]
print("Original List: ")
print(lst)
roll_lst=[]
name_lst=[]
age_lst=[]
for i in lst:
  roll_lst.append(i[0])
  name_lst.append(i[1])
  age_lst.append(i[2])
print("Roll Numbers: ", roll_lst)
print("Names: ", name_lst)
print("Ages: ", age_lst)
