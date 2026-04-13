import os,sys
flrname = input("Enter a file name to read the content.")
if os.path.isfile(flrname):
  fr = open(flrname,"r")
else:
  print(flrname, "doesn't exists.")
  sys.exit()

flwname = input("Enter a file name to write the content.")
fw = open(flwname,"w")
ch = fr.read(1)

while ch:
  print(ch, end = "",file = fw)
  ch = fr.read(1)
fr.close()
fw.close()
print(flrname, "is copied to", flwname, "successfully.")
