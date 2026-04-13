from datetime import date
d1=(16,2,2026)
d2=(24,3,2026)
date1= date(d1[2],d1[1],d1[0])
date2= date(d2[2],d2[1],d2[0])
days=abs((date2-date1).days)
print("Date1:", d1)
print("Date2:", d2)
print("Number of days between two dates: ", days)
