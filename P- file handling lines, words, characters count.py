import os,sys
flrname = input("Enter a file name to count no. of lines, words and characters: ")
if os.path.isfile(flrname):
  fr = open(flrname, "r")
else:
  print(flrname, "doesn't exists.")
  sys.exit()

cl=cw=cc=0
for line in fr:
  words = line.split()
  cl = cl + 1
  cw = cw + len(words)
  cc = cc + len(line)

print("No. of line(s)=",cl)
print("No. of word(s)=",cw)
print("No. of character(s)=",cc)
fr.close()
