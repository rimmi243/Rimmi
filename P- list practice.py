lst1 = [72, 60, 58, 52, 54, 56]
lst3 = lst2 = lst1
lst1 = []
print(lst1, lst2, lst3)
print(lst2 is lst3)
lst2.clear()
print(lst2, lst3)
