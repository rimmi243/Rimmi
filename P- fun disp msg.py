def fun():
  print("fun executed")
def disp():
  print("disp executed")
def msg():
  print("msg executed")
lst = [fun, disp, msg]
for f in lst:
  f()
