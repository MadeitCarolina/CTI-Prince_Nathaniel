# P3HW2_Salary_LastnameFirstname.py

# Author: [Your Full Name]
# Date: [Current Date]
# Assignment Name: P3HW2 - Salary Calculation with Overtime
# Description: This program calculates the gross pay for an employee, including overtime pay if applicable.

# Step 1: Ask the user for the employee's name
employee_name = input("Enter the employee's name: ")

# Step 2: Ask the user for the number of hours worked this week
hours_worked = float(input("Enter the number of hours worked this week: "))

# Step 3: Ask the user for the employee's hourly pay rate
pay_rate = float(input("Enter the employee's hourly pay rate: "))

# Step 4: Check for overtime (more than 40 hours)
if hours_worked > 40:
    overtime_hours = hours_worked - 40  # Calculate overtime hours
    overtime_pay = overtime_hours * (pay_rate * 1.5)  # Calculate overtime pay (time and a half)
    regular_hours = 40  # The first 40 hours are regular hours
else:
    overtime_hours = 0  # No overtime if hours worked is 40 or less
    overtime_pay = 0
    regular_hours = hours_worked  # All hours are regular hours

# Step 5: Calculate regular pay (up to 40 hours)
regular_pay = regular_hours * pay_rate

# Step 6: Calculate the gross pay (regular pay + overtime pay)
gross_pay = regular_pay + overtime_pay

# Step 7: Display the results
print("\nEmployee Pay Information:")
print(f"Employee Name: {employee_name}")
print(f"Hourly Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked:.2f}")
print(f"Overtime Hours: {overtime_hours:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
