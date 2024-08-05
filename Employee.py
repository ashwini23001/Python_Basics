class Employee:
    def __init__(self, name, code, basic):
        self.name = name
        self.code = code
        self.basic = basic

    def display(self):
        print("Name of the employee: ", self.name)
        print("Employee Code: ", self.code)
        print("Basic pay: ", self.basic)

        # let DA be 10% of basic pay, HRA be 20% Of the basic pay, PF be 12% of basic pay
        DA = (10 / 100) * self.basic
        HRA = (20 / 100) * self.basic
        PF = (12 / 100) * self.basic
        net = (self.basic + DA + HRA) - PF
        print("DA: ", DA)
        print("HRA: ", HRA)
        print("PF: ", PF)
        print("Net Salary: ", net)


n = int(input("How many employees? "))
employees = []

for i in range(n):
    name = input(f"Enter the name of Employee {i + 1}: ")
    code = int(input(f"Enter the code for Employee {i + 1}: "))
    basic = float(input(f"Enter the Basic Pay for Employee {i + 1}: "))
    employee = Employee(name, code, basic)
    employees.append(employee)

for employee in employees:
    employee.display()
    print()  
