import csv

salaries = open('employeepay.csv', 'r')

csv_file = csv.reader(salaries)

next(csv_file) #Skips header row

for rec in csv_file:
    salary = float(rec[3])
    bonus = salary * float(rec[4])
    total_pay = salary + bonus

    print(f"first name: {rec[1]}")
    print(f"last name: {rec[2]}")
    print(f"Salary: ${salary:>10,.2f}")
    print(f"Bonus:  ${bonus:>10,.2f}")
    print(f"Pay:    ${total_pay:>10,.2f}")
    input()

salaries.close()