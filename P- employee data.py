employee_data = [
   {'dept_no': 101, 'roll_no': 1, 'salary': 30000},
   {'dept_no': 101, 'roll_no': 2, 'salary': 40000},
   {'dept_no': 101, 'roll_no': 3, 'salary': 25000},
   {'dept_no': 102, 'roll_no': 4, 'salary': 50000},
   {'dept_no': 102, 'roll_no': 5, 'salary': 55000},
   {'dept_no': 102, 'roll_no': 6, 'salary': 60000},
   {'dept_no': 103, 'roll_no': 7, 'salary': 35000},
   {'dept_no': 103, 'roll_no': 8, 'salary': 45000}
   ]

for emp in employee_data:
  dept = emp["dept_no"]
  salary = emp["salary"]

min_salary = min(salary)
max_salary = max(salary)

print(min_salary)
print(max_salary)


