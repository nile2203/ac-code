from app.models import Department, db
from app.employee.employee import EmployeeEntity


class DepartmentEntity:
    def __init__(self, department):
        self.department = department

    @staticmethod
    def does_exists(name):
        if Department.query.filter_by(name=name).first():
            return 1

        return 0

    @staticmethod
    def create(name):
        if DepartmentEntity.does_exists(name) == 1:
            return 0, 'Department already exists', None

        department = Department(name=name)
        db.session.add(department)
        db.session.commit()
        return 1, 'Department created successfully', DepartmentEntity(department=department).get_serialized()

    @staticmethod
    def get_by_id(department_id):
        department = Department.query.filter_by(id=department_id).first()
        return DepartmentEntity(department=department) if department else None

    def update(self, name, employee_ids):
        if name:
            self.department.name = name

        if employee_ids:
            for employee_id in employee_ids:
                employee_entity = EmployeeEntity.get_by_id(employee_id)
                if not employee_entity:
                    continue

                self.department.employees.append(employee_entity.get())

        db.session.add(self.department)
        db.session.commit()
        return 1, 'Object updated', self.get_serialized()

    def delete(self):
        db.session.delete(self.department)
        db.session.commit()
        return 1, 'Department removed'

    def get(self):
        return self.department

    def get_serialized(self):
        return {
            'name': self.department.name,
            'id': self.department.id,
            'employees': EmployeeEntity.get_all_serialized(self.department.employees)
        }
