# 🧑‍💼 Employee Management System

A command-line based **Employee Management System** written in Python that supports managing different types of employees such as Managers, Developers, and Freelancers. The system demonstrates object-oriented programming concepts like inheritance and multiple inheritance, and stores employee data in a JSON file.


## 📋 Features

- ✅ Add Employees with roles: Manager, Developer, Freelancer
- 👀 View all Employees with detailed information
- 🗑️ Remove Employees by Employee ID
- 💾 Persistent data storage using `Employees.json`
- 🔄 Role-specific fields (e.g., Team Size, Programming Language, Hours Worked, Hourly Rate)




## 🛠️ Requirements

- Python 3.x



## 🚀 How to Run

1. Clone the repository or download the source code file.
2. Open a terminal or command prompt.
3. Run the script using:

```bash
python EmployeeManagement.py
```



## 📋 Role Details
| Role       | Extra Input(s)            | Example Input |
| ---------- | ------------------------- | ------------- |
| Manager    | Team Size (integer)       | 5             |
| Developer  | Programming Language      | Python        |
| Freelancer | Hours Worked, Hourly Rate | 20, 50        |




## 💾 Data Storage Format
Employees are saved in a file named Employees.json in JSON format. Each employee is stored as an object with the following structure:
```bash
{
    "type": "Freelancer",
    "eid": "E123",
    "name": "Alice",
    "department": "Design",
    "extra": [20, 50]
}
```

"type": The employee class name, used to instantiate the correct object.

"extra": Role-specific data, e.g., team size for managers, language for developers, or hours and rate for freelancers.



## ❗ Business Rules & Notes
🔢 Employee IDs must be unique.

📂 If Employees.json does not exist, it will be automatically created.

🛡️ Input validation is performed for roles and numeric fields.

📝 Role-specific inputs must be valid (e.g., numeric for team size, hours, and rate).

🧹 Data is loaded fresh from the JSON file whenever the system displays employees or performs operations, ensuring data consistency.