from flask import redirect, request, render_template
from model.models import Employees
from app import app, db



@app.route('/selectemployees')
def select_employees():
    employees = Employees.query.order_by(Employees.date.desc()).all()
    return render_template("select_employees.html", employees=employees)


@app.route('/selectemployees/<int:employee_id>')
def select_detailemp(employee_id):
    employee = Employees.query.get(employee_id)
    return render_template("select_detailemp.html", employee=employee)


@app.route('/selectemployees/<int:employee_id>/deleteemployees')
def select_delete_employees(employee_id):
    employee = Employees.query.get_or_404(employee_id)

    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/selectemployees')
    except:
        return "При видаленні даних сталась помилка"


@app.route('/selectemployees/<int:employee_id>/updateemployees', methods=['POST', 'GET'])
def update_employees(employee_id):
    employee = Employees.query.get(employee_id)
    if request.method == "POST":
        employee.first_name = request.form['first_name']
        employee.last_name = request.form['last_name']
        employee.email = request.form['email']
        employee.salary = request.form['salary']
        employee.department_id = request.form['department_id']

        try:
            db.session.commit()
            return redirect('/selectemployees')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("update-employees.html", employee=employee)


@app.route('/create-employees', methods=['POST', 'GET'])
def create_employees():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salary = request.form['salary']
        department_id = request.form['department_id']

        employees = Employees(first_name=first_name, last_name=last_name, email=email, salary=salary, department_id=department_id)

        try:
            db.session.add(employees)
            db.session.commit()
            return redirect('/')
        except:
            return "При заповненні вийшла помилка"
    else:
        return render_template("create-employees.html")