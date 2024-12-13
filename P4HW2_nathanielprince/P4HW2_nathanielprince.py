# Your Name: [Your Full Name]
# Date: [Date]
# Assignment Name: P4HW2
# A brief description of the project:
# This program calculates the gross pay for multiple employees, including overtime pay,
# regular pay, and total amounts for all employees. The user can enter employee details
# until they choose to stop by typing "Done".

# Initialize variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Program start message
print("Welcome to the Employee Pay Calculation Program")

# Start the loop to gather employee information
while True:
    # Ask for employee's name
    employee_name = input("Enter employee's name or type 'Done' to stop: ")
    
    # If user types "Done", stop the program
    if employee_name.lower() == "done":
        break
    
    # Ask for the hourly pay rate and hours worked
    pay_rate = float(input(f"Enter {employee_name}'s hourly pay rate: $"))
    hours_worked = float(input(f"Enter {employee_name}'s hours worked: "))
    
    # Calculate regular pay and overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
    
    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += (regular_pay + overtime_pay)
    employee_count += 1

# Display the results
print("\nTotal Overtime Pay: $", round(total_overtime_pay, 2))
print("Total Regular Pay: $", round(total_regular_pay, 2))
print("Total Gross Pay for all employees: $", round(total_gross_pay, 2))
print("Total number of employees entered:", employee_count)
