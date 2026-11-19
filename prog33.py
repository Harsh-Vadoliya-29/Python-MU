class Employee:
    company = "TechCorp"
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

e1 = Employee("Aarav", 50000)
e2 = Employee("Priya", 60000)
e1.display()
e2.display()
print(f"Total employees: {Employee.count}")
