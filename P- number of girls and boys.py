lst=["Aarti", "Neha", ("Aman", "Amit", "Sam"), "Meena", "Tina", "Khushi", "Tanvi", ("Ram", "Shyam")]
print("Original List: ")
print(lst)
count1=0
count2=0
for i in lst:
  if isinstance(i, tuple):
    for j in i:
      count1 = count1 + 1
  else:
    count2 = count2 + 1
print("Number of boys: ", count1)
print("Number of girls: ", count2)
