a= int(input("enter a year:"))
if ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)):
       print("entered year is a leap year")
else:
  print("entered year is not a leap year")
