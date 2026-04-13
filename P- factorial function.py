def fact(n):
    ans = 1
    for i in range (1, n+1):
        ans = ans * i
    return ans

num = int(input("Enter a number: "))
ans = fact(num)
print(ans)
