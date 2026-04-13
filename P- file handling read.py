import os,sys
flname = input("Enter a file name to read the content.")
if os.path.isfile(flname):
  f = open(flname,"r")
else:
  print(flname,"doesn't exists.")
  sys.exit()
ch = f.read(1)

while ch:
  print(ch,end="")
  ch = f.read(1)
f.close()
