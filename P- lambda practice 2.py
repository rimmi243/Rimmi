p = lambda n: n**3
q = lambda a,b,c: (a+b+c)/3
r = lambda str: str.strip().upper()
print(p(4))
print(q(10,20,30))
print(r("pDeU"))


lst1= [10,20,30,40,50]
print((lambda l: sum(l)/len(l))(lst1))
