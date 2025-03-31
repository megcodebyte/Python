def Annual():
    annual_salary = float(input("Please enter your annual salary: "))
    hourly_salary = annual_salary / (40 * 52)
    print(f"Your hourly rate: ${round(hourly_salary, 2)}")
    
def Hourly ():
    hourly_salary = float(input("Please enter your hourly salary: "))
    annual_salary = hourly_salary * 40 * 52
    print(f"Your annual rate: ${round(annual_salary, 2)}")
    
num = int(input("Please choose:\n1:Annual to Hourly\n2:Hourly to Annual\n"))
if num == 1:
    Annual()
else:
    Hourly()