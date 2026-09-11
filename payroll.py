# prompt the user for employee details
employee_id=int(input("Enter employee ID: "))
employee_name=input("Enter employee name: ")
basic_salary=float(input("Enter basic salary: "))
allowances=float(input("Enter allowances: "))
deductions=float(input("Enter deductions: "))
tax_rate=float(input("enter tax rate "))
tax_rate=0.1
# calculationof gross salary,tax amount and net salary
gross_salary=basic_salary+allowances
tax_amount=gross_salary*tax_rate
net_salary=gross_salary-tax_amount-deductions
# display the results
print("employee_id:", employee_id)
print("employee_name:", employee_name)
print("basic_salary:", basic_salary)
print("allowances:", allowances)
print("deductions:", deductions)
print("gross_salary:", gross_salary)
print("tax_amount:", tax_amount)
print("net_salary:", net_salary)