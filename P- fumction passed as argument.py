def add(a,b,c):
  c()
  print(a+b)
def print_a_word():
  print("PDEU")
f = print_a_word
add(25,30,f)
