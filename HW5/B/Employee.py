import re

class Employee:
    def __init__(self, id, fullname, birthday, phone, email, employee_type):
        self.id = id
        self.fullname = fullname
        self.birthday = birthday
        self.phone = phone
        self.email = email
        self.employee_type = employee_type #0 is experienced, 1 is fresher, 2 is intern
        self.employee_count = 0 
    
    def check_legitimacy(self):
        try:
            # Check email legitimacy
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, self.email):
                raise ValueError("Invalid email format")

            # Check phone legitimacy (assuming a simple format of 10 digits)
            phone_pattern = r'^\d{10}$'
            if not re.match(phone_pattern, self.phone):
                raise ValueError("Invalid phone number format")

            # Check name legitimacy (allowing letters, spaces, and hyphens)
            name_pattern = r'^[a-zA-Z\s-]+$'
            if not re.match(name_pattern, self.fullname):
                raise ValueError("Invalid name format")

            # Check birthday legitimacy (assuming format: YYYY-MM-DD)
            birthday_pattern = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(birthday_pattern, self.birthday):
                raise ValueError("Invalid birthday format")

            return True
        except ValueError as e:
            print(f"Validation error: {str(e)}")
            return False

    def showInfo(self):
        print("id: ", self.id)
        print("fullname: ", self.fullname)
        print("birthday: ", self.birthday)
        print("phone: ", self.phone)
        print("email: ", self.email)
        print("employee_type: ", self.employee_type)
        print("employee_count: ", self.employee_count)

    @classmethod
    def add_employee(self, cls, id, fullname, birthday, phone, email, employee_type):
        new_employee = cls(id, fullname, birthday, phone, email, employee_type)
        if new_employee.check_legitimacy():
            self.employee_count += 1
            return new_employee
        else:
            return None
    
    @classmethod
    def find_experienced_employees(cls, employees):
        return [emp for emp in employees if emp.employee_type == 0]
    
    @classmethod
    def find_fresher_employees(cls, employees):
        return [emp for emp in employees if emp.employee_type == 1]
    
    @classmethod
    def find_intern_employees(cls, employees):
        return [emp for emp in employees if emp.employee_type == 2]
