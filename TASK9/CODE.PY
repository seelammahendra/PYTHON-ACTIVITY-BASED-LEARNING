


employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")


basic_pay = float(input("Enter Basic Pay (₹): "))
allowances = float(input("Enter Total Allowances (₹): "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate per Hour (₹): "))
incentives = float(input("Enter Incentives (₹): "))


overtime_pay = overtime_hours * overtime_rate


gross_salary = basic_pay + allowances + overtime_pay + incentives


if gross_salary <= 20000:
    income_tax = 0
elif gross_salary <= 40000:
    income_tax = (gross_salary - 20000) * 0.05
else:
    income_tax = (20000 * 0.05) + ((gross_salary - 40000) * 0.10)


if gross_salary > 15000:
    professional_tax = 200
else:
    professional_tax = 0


total_deductions = income_tax + professional_tax


net_salary = gross_salary - total_deductions


print("\n" + "=" * 45)
print("             SALARY STATEMENT")
print("=" * 45)
print(f"Employee ID          : {employee_id}")
print(f"Employee Name        : {employee_name}")
print("-" * 45)
print(f"Basic Pay            : ₹{basic_pay:,.2f}")
print(f"Allowances           : ₹{allowances:,.2f}")
print(f"Overtime Pay         : ₹{overtime_pay:,.2f}")
print(f"Incentives           : ₹{incentives:,.2f}")
print("-" * 45)
print(f"Gross Salary         : ₹{gross_salary:,.2f}")
print("-" * 45)
print(f"Progressive Income Tax: ₹{income_tax:,.2f}")
print(f"Professional Tax     : ₹{professional_tax:,.2f}")
print(f"Total Deductions     : ₹{total_deductions:,.2f}")
print("-" * 45)
print(f"NET SALARY           : ₹{net_salary:,.2f}")
print("=" * 45)
