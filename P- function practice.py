def fun(n1,n2):
    print("Beginning of function.")
    print(n1, n2, n1+n2, n1-n2)
    print("End of function.")
    return n1*n2

print("Before function call")
no1 = int(input("Enter number 1: "))
no2 = int(input("Enter number 2: "))
print(fun(no1,no2))
print("After function call")
