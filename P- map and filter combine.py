lst = [10,20,30,40,50]
result = list(filter(lambda x: x>1000,map(lambda x:x*x,lst)))
print(result)
