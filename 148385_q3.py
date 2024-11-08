# Define the Employee class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name}. New salary: {self.salary}")

# Define the Department class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee '{employee.name}' added to the department '{self.department_name}'.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for '{self.department_name}': {total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"\nEmployees in Department '{self.department_name}':")
        if not self.employees:
            print("No employees in this department yet.")
        for employee in self.employees:
            employee.display_details()

# Interactive code for adding employees and displaying total salary
def main():
    # Create a department
    department = Department("Human Resources")

    # Adding employees interactively
    while True:
        name = input("Enter employee name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter employee salary: "))

        # Create an Employee object and add to the department
        employee = Employee(name, employee_id, salary)
        department.add_employee(employee)

    # Display all employees in the department
    department.display_all_employees()

    # Calculate and display total salary expenditure
    department.calculate_total_salary()

# Run the interactive code
main()
