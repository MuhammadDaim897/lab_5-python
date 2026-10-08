
# Ask the user to enter information for 3 employees:

employees = []
for i in range(3):
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nEmployee Information:")

for employee in employees:
    print(employee)

