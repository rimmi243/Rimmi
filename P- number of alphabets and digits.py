str= input("enter a string: ")
alphabet_count = 0
digit_count = 0
for char in str:
  if char.isalpha():
    alphabet_count += 1
  elif char.isdigit():
    digit_count += 1
print("number of alphabets: ")
print(alphabet_count)
print("number of digits: ")
print(digit_count)
