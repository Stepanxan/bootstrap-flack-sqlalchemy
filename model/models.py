from app import db
from datetime import datetime


class Departments(db.Model):
    __tablename__ = "departments"
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(200), nullable=False)
    manager_id = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<departments {self.id}>"


class Employees(db.Model):
    __tablename__ = "employees"
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<employees {self.id}>"