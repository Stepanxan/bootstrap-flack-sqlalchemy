from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:19982804@localhost:3306/stepanproject_db'
db = SQLAlchemy(app)
db.init_app(app)


class Departments(db.Model):
    departmentID = db.Column(db.Integer, primary_key=True)
    departmentNAME = db.Column(db.String(200), nullable=False)
    managerID = db.Column(db.Integer, nullable=False)
    locationID = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<departments {self.id}>"


class Employees(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    departmentID = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<employees {self.id}>"

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/selectdepartments')
def select_departments():
    departments = Departments.query.order_by(Departments.date.desc()).all()
    return render_template("select-departments.html", departments=departments)


@app.route('/selectdepartments/<int:departmentID>')
def select_detail(departmentID):
    department = Departments.query.get(departmentID)
    return render_template("select_detail.html", department=department)


@app.route('/selectdepartments/<int:departmentID>/deletedepartments')
def select_delete_department(departmentID):
    department = Departments.query.get_or_404(departmentID)

    try:
        db.session.delete(department)
        db.session.commit()
        return redirect('/selectdepartments')
    except:
        return "При видаленні даних сталась помилка"


@app.route('/selectdepartments/<int:departmentID>/updatedepartments', methods=['POST', 'GET'])
def update_departments(departmentID):
    department = Departments.query.get(departmentID)
    if request.method == "POST":
        department.departmentNAME = request.form['departmentNAME']
        department.managerID = request.form['managerID']
        department.locationID = request.form['locationID']

        try:
            db.session.commit()
            return redirect('/selectdepartments')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("update-departments.html", department=department)

@app.route('/selectemployees')
def select_employees():
    employees = Employees.query.order_by(Employees.date.desc()).all()
    return render_template("select_employees.html", employees=employees)


@app.route('/selectemployees/<int:employeeID>')
def select_detailemp(employeeID):
    employee = Employees.query.get(employeeID)
    return render_template("select_detailemp.html", employee=employee)


@app.route('/selectemployees/<int:employeeID>/deleteemployees')
def select_delete_employees(employeeID):
    employee = Employees.query.get_or_404(employeeID)

    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/selectemployees')
    except:
        return "При видаленні даних сталась помилка"


@app.route('/selectemployees/<int:employeeID>/updateemployees', methods=['POST', 'GET'])
def update_employees(employeeID):
    employee = Employees.query.get(employeeID)
    if request.method == "POST":
        employee.first_name = request.form['first_name']
        employee.last_name = request.form['last_name']
        employee.email = request.form['email']
        employee.salary = request.form['salary']
        employee.departmentID = request.form['departmentID']

        try:
            db.session.commit()
            return redirect('/selectemployees')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("update-employees.html", employee=employee)


@app.route('/create-departments', methods=['POST', 'GET'])
def create_departments():
    if request.method == "POST":
        departmentNAME = request.form['departmentNAME']
        managerID = request.form['managerID']
        locationID = request.form['locationID']

        department = Departments(departmentNAME=departmentNAME, managerID=managerID, locationID=locationID)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("create-departments.html")


@app.route('/create-employees', methods=['POST', 'GET'])
def create_employees():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salary = request.form['salary']
        departmentID = request.form['departmentID']

        employees = Employees(first_name=first_name, last_name=last_name, email=email, salary=salary, departmentID=departmentID)

        try:
            db.session.add(employees)
            db.session.commit()
            return redirect('/')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("create-employees.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)