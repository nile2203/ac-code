from app import db


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60))
    department = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __repr__(self):
        return '<Employee: {} {}>'.format(self.id, self.email)


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)
    employees = db.relationship('Employee', backref='employee')

    def __repr__(self):
        return '<Department: {} {}>'.format(self.id, self.name)
