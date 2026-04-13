def count_lower_upper(string):
    lower_count = 0
    upper_count = 0

    for char in str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count


str = input("Enter a string: ")

result = count_lower_upper(str)

print(f"Original string: {str}")
print(f"Counts: {result}")
