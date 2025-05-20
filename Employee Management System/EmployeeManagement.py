import json
import os

class Employee:
    def __init__(self, eid, name, department):
        self.eid = eid
        self.name = name
        self.department = department
    
    def display_info(self):
        print(f"\nEmployee id: {self.eid} \nName: {self.name} | Department: {self.department}")


class Manager (Employee):
    def __init__(self, eid, name, department, team_size):
        super().__init__(eid, name, department)
        self.team_size = team_size

    def display_info(self):
        print(f"\nEmployee id: {self.eid} \nName: {self.name} | Role: Manager | Team Size: {self.team_size}")


class Developer (Employee):
    def __init__(self, eid, name, department, language):
        super().__init__(eid, name, department)
        self.language = language
    
    def display_info(self):
        print(f"\nEmployee id: {self.eid} \nName: {self.name} | Role: Developer | Language: {self.language}")


class Contractor:
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate


class Freelancer (Employee, Contractor):
    def __init__(self, eid, name, department, hours_worked, hourly_rate):
        Employee.__init__(self, eid, name, department)
        Contractor.__init__(self, hours_worked, hourly_rate)

    def display_info(self):
        super().display_info()
        print(f"Role: Freelancer | Hours Worked: {self.hours_worked} | Hour rate: {self.hourly_rate} | Payment: $ {self.calculate_payment()}")


class EmployeeManagement:
    def __init__(self, filename=None):
        if filename is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(base_dir, "Employees.json")
        self.employee = []
        self.filename = filename
        self.load_data()
    
    def show_all_employee(self):
        self.load_data()
        if not self.employee:
            print("Employee Library is empty.")
        else:
            for employee in self.employee:
                employee.display_info()

    
    def add_employee(self, employee):
        self.employee.append(employee)
        self.save_employee_to_file(employee)
        print(f"Employee '{employee.name}' added successfully!")
    
    def load_data(self):
        self.employee.clear()
        for employee in self.load_all_from_file():
            emp_type = employee["type"]
            eid = employee["eid"]
            name = employee["name"]
            department = employee["department"]
            extra_data = employee["extra"]

            if emp_type == "Manager":
                self.employee.append(Manager(eid, name, department, extra_data))
            elif emp_type == "Developer":
                self.employee.append(Developer(eid, name, department, extra_data))
            elif emp_type == "Freelancer":
                hours_worked, hourly_rate = extra_data
                self.employee.append(Freelancer(eid, name, department, hours_worked, hourly_rate))

    def load_all_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_employee_to_file(self, employee):
        emp_data = {
            "type": type(employee).__name__,
            "eid": employee.eid,
            "name": employee.name,
            "department": employee.department
        }

        # Add the extra field
        if isinstance(employee, Manager):
            emp_data["extra"] = employee.team_size
        elif isinstance(employee, Developer):
            emp_data["extra"] = employee.language
        elif isinstance(employee, Freelancer):
            emp_data["extra"] = employee.hours_worked,employee.hourly_rate

        # Append to file
        all_data = self.load_all_from_file()
        all_data.append(emp_data)
        with open(self.filename, "w") as f:
            json.dump(all_data, f, indent=4)
    
    def remove_employee_by_id(self, eid):
        all_employees = self.load_all_from_file()
        updated_employees = []
        for emp in all_employees:
            if emp["eid"] != eid:
                updated_employees.append(emp)

        if len(all_employees) == len(updated_employees):
            print(f"No employee found with ID: {eid}")
        else:
            with open(self.filename, "w") as f:
                json.dump(updated_employees, f, indent=4)
            print(f"Employee {eid} removed successfully!")


emp = EmployeeManagement()

# Menu loop
while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("\n1. Add Employee")
    print("2. View All Employees")
    print("3. Remove Employee")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice of operation(1–4): "))
    except ValueError:
        print("Invalid input. Please enter your correct choice of operation.")
        continue

    if choice == 1:
        while True:

            print("\nSelect Role to Add:")
            print("1. Manager")
            print("2. Developer")
            print("3. Freelancer")

            roleDictionary = {
                1: ("Manager", Manager , ["Team Size"]),
                2: ("Developer", Developer, ["Language"]),
                3: ("Freelancer", Freelancer , ["Hours", "Rate"])
            }

            try:
                role = int(input("Enter choice for role (1–3): "))
                if role not in roleDictionary:
                    raise ValueError
                break
            except ValueError:
                print("\nPlease provide the correct role.")
        
        while True:
            eid = input("Enter Employee ID: ")

            dataCheck = emp.load_all_from_file()

            # Check if eid already exists
            exists = False
            for emp in dataCheck:
                if emp["eid"] == eid:
                    exists = True
                    break

            try:
                if exists:
                    raise ValueError
                break
            except ValueError:
                print("Employee ID already exist.")

        name = input("Enter Name: ")
        department = input("Enter Department: ")

        role_name = roleDictionary[role][0]
        className = roleDictionary[role][1]
        extra_fields = roleDictionary[role][2]
        extra_inputs = []

        for field in extra_fields:
            value = input(f"Enter {field} of {role_name.lower()}: ")

            try:
                value = int(value)
            except:
                pass
            
            extra_inputs.append(value)

        employee = className(eid, name, department, *extra_inputs)
        emp.save_employee_to_file(employee)

    
    elif choice == 2:
        emp.show_all_employee()

    elif choice == 3:
        eid = input("Enter Employee ID to remove: ")
        emp.remove_employee_by_id(eid)

    elif choice == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
