def sum_avg():
    print("Emter marks of 5 subjects:")
    a = int(input("Subject1: "))
    b = int(input("Subject2: "))
    c = int(input("Subject3: "))
    d = int(input("Subject4: "))
    e = int(input("Subject5: "))

    total = a+b+c+d+e
    average = total/5

    return total, average

total_marks, average_marks = sum_avg()
print("-" * 30)
print(f"Total marks are: {total_marks}")
print(f"Average marks are: {average_marks}")
    
