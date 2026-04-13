print("24 hours of a day: ")
for hour in range(24):
   if hour == 0:
     print("12 Midnight")
   elif hour == 12:
     print("12 Noon")
   elif hour < 12:
     print(f"'{hour}' AM ")
   else:
     print(" '{hour}' PM "
