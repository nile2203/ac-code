from app.models import Employee, db


class EmployeeEntity:
    def __init__(self, employee):
        self.employee = employee

    @staticmethod
    def get_by_id(employee_id):
        employee = Employee.query.filter_by(id=employee_id).first()
        return EmployeeEntity(employee=employee) if employee else None

    @staticmethod
    def does_exists(email):
        if Employee.query.filter_by(email=email).first():
            return 1

        return 0

    @staticmethod
    def create(email, first_name, last_name, department_id):
        if EmployeeEntity.does_exists(email) == 1:
            return 0, 'Employee already exists', None

        employee = Employee(email=email, first_name=first_name, last_name=last_name, department=department_id)
        db.session.add(employee)
        db.session.commit()
        return 1, 'Employee created successfully', EmployeeEntity(employee=employee).get_serialized()

    @staticmethod
    def get_all_serialized(employees):
        serialized = []
        for employee in employees:
            serialized.append(EmployeeEntity(employee=employee).get_serialized())

        return serialized

    def get_serialized(self):
        return {
            'id': self.employee.id,
            'email': self.employee.email,
            'first_name': self.employee.first_name,
            'last_name': self.employee.last_name,
            'department_id': self.employee.department
        }

    def get(self):
        return self.employee

    def update(self, first_name, last_name, department):
        self.employee.first_name = self.employee.first_name or first_name
        self.employee.last_name = self.employee.last_name or last_name
        self.employee.department = self.employee.department or department
        db.session.add(self.employee)
        db.session.commit()

        return 1, 'Object updated', self.get_serialized()

    def delete(self):
        db.session.delete(self.employee)
        db.session.commit()
        return 1, 'Employee deleted'

